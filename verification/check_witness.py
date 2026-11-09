#!/usr/bin/env python3
"""Deterministic convention checks for the thermal contact witness.

Run from the repository root:
    python verification/check_witness.py

This script does not test or prove the uniform operational theorem. It compares
independent numerical representations at the fixed parameters documented in
verification/README.md and exits nonzero on a failed check.
"""

from __future__ import annotations

import json
import math
import platform
import warnings

import numpy as np
import scipy
from scipy.integrate import IntegrationWarning, quad
from scipy.linalg import expm


QUAD_ABS = 1.0e-11
QUAD_REL = 1.0e-11
MATRIX_TOL = 2.0e-11
PHASE_TOL = 2.0e-8


def integrate(function, lower, upper):
    value, estimate = quad(
        function, lower, upper, epsabs=QUAD_ABS, epsrel=QUAD_REL, limit=400
    )
    return float(value), float(estimate)


def require_close(label, actual, expected, tolerance):
    error = abs(actual - expected)
    if not math.isfinite(float(error)) or error > tolerance:
        raise AssertionError(
            f"{label}: error {error:.16g} exceeds tolerance {tolerance:.16g}"
        )
    return float(error)


def complex_pair(value):
    return {"real": float(value.real), "imag": float(value.imag)}


def finite_oscillator_coherence(dimension, omega, coupling, beta, h):
    """Trace U_(++) rho_beta U_(+-)^dagger from Hamiltonian matrices."""
    annihilation = np.diag(np.sqrt(np.arange(1, dimension, dtype=float)), 1)
    number = annihilation.T @ annihilation
    bath_hamiltonian = omega * number
    field = coupling * (annihilation + annihilation.T)
    weights = np.exp(-beta * omega * np.arange(dimension, dtype=float))
    thermal_state = np.diag(weights / weights.sum())
    plus = expm(-1j * (bath_hamiltonian + field) * h)
    minus = expm(-1j * (bath_hamiltonian - field) * h)
    branch_zero = plus @ plus
    branch_one = minus @ plus
    return complex(np.trace(branch_zero @ thermal_state @ branch_one.conj().T))


def oscillator_check():
    omega, coupling, beta, h = 1.0, 0.3, 1.0, 0.4
    phase = (
        4.0
        * coupling**2
        * (2.0 * math.sin(omega * h) - math.sin(2.0 * omega * h))
        / omega**2
    )
    exponent = (
        4.0
        * coupling**2
        / math.tanh(beta * omega / 2.0)
        * (1.0 - math.cos(omega * h))
        / omega**2
    )
    exact = complex(np.exp(-exponent + 1j * phase))
    coarse = finite_oscillator_coherence(40, omega, coupling, beta, h)
    fine = finite_oscillator_coherence(60, omega, coupling, beta, h)
    fine_error = require_close("60-level oscillator", fine, exact, MATRIX_TOL)
    change = require_close("40/60-level stability", coarse, fine, MATRIX_TOL)
    return {
        "parameters": {"omega": omega, "coupling": coupling, "beta": beta, "h": h},
        "fock_dimensions": [40, 60],
        "analytic_coherence": complex_pair(exact),
        "matrix_coherence_60": complex_pair(fine),
        "analytic_phase": phase,
        "absolute_error_60": fine_error,
        "absolute_change_40_to_60": change,
        "tolerance": MATRIX_TOL,
    }


def spectral_density(omega, gamma, beta):
    return gamma / math.pi * math.tanh(beta * omega / 2.0)


def cutoff_phase_frequency(gamma, beta, h, cutoff):
    def integrand(omega):
        # Stable form of (2 sin(omega h) - sin(2 omega h)) / omega^2.
        # numpy.sinc(x) means sin(pi*x)/(pi*x), including its value at zero.
        pulse_factor = h**2 * math.sin(omega * h) * np.sinc(omega * h / (2.0 * math.pi)) ** 2
        return 4.0 * spectral_density(omega, gamma, beta) * pulse_factor

    return integrate(integrand, 0.0, cutoff)


def cutoff_phase_time(gamma, beta, h, cutoff):
    def response(u):
        return integrate(
            lambda omega: spectral_density(omega, gamma, beta) * math.sin(omega * u),
            0.0,
            cutoff,
        )[0]

    first, first_error = integrate(lambda u: u * response(u), 0.0, h)
    second, second_error = integrate(lambda u: (2.0 * h - u) * response(u), h, 2.0 * h)
    return 4.0 * (first + second), 4.0 * (first_error + second_error)


def limiting_phase(gamma, beta, h):
    def response(u):
        x = math.pi * u / beta
        if x > 700.0:
            return 0.0
        return gamma / beta / math.sinh(x)

    def first_integrand(u):
        if u == 0.0:
            return gamma / math.pi
        return u * response(u)

    first, first_error = integrate(first_integrand, 0.0, h)
    second, second_error = integrate(lambda u: (2.0 * h - u) * response(u), h, 2.0 * h)
    return 4.0 * (first + second), 4.0 * (first_error + second_error)


def cutoff_free_exponent(gamma, duration, cutoff):
    def integrand(omega):
        # Stable form of 4 gamma/pi * (1 - cos(omega*duration))/omega^2.
        return (
            2.0
            * gamma
            * duration**2
            / math.pi
            * np.sinc(omega * duration / (2.0 * math.pi)) ** 2
        )

    return integrate(integrand, 0.0, cutoff)


def cutoff_check():
    gamma, beta = 1.0, 0.4
    horizon = 1.0 / gamma
    h = horizon / 2.0
    frequency_phase, frequency_error = cutoff_phase_frequency(gamma, beta, h, 16.0)
    time_phase, time_error = cutoff_phase_time(gamma, beta, h, 16.0)
    representation_error = require_close(
        "cutoff phase, frequency versus time", frequency_phase, time_phase, PHASE_TOL
    )
    limit_phase, limit_error = limiting_phase(gamma, beta, h)
    markov_coherence = math.exp(-2.0 * gamma * h)
    limit_coherence = complex(np.exp(-2.0 * gamma * h + 1j * limit_phase))
    rows = []
    for cutoff in (16.0, 64.0, 256.0):
        phase, phase_error = cutoff_phase_frequency(gamma, beta, h, cutoff)
        exponent, exponent_error = cutoff_free_exponent(gamma, h, cutoff)
        free_exponent, free_error = cutoff_free_exponent(gamma, horizon, cutoff)
        coherence = complex(np.exp(-exponent + 1j * phase))
        deficit = 2.0 * gamma * horizon - free_exponent
        analytic_tail_bound = 8.0 * gamma / (math.pi * cutoff)
        if deficit < -PHASE_TOL or deficit > analytic_tail_bound + PHASE_TOL:
            raise AssertionError("free-channel exponent deficit violates its analytic tail bound")
        rows.append(
            {
                "cutoff": cutoff,
                "witness_phase": phase,
                "witness_exponent": exponent,
                "witness_distance_to_markov": float(abs(coherence - markov_coherence) / 2.0),
                "witness_distance_to_limit": float(abs(coherence - limit_coherence) / 2.0),
                "free_exponent_deficit_at_horizon": deficit,
                "uniform_free_exponent_tail_bound": analytic_tail_bound,
                "quadrature_error_estimates": [phase_error, exponent_error, free_error],
            }
        )
    return {
        "parameters": {"gamma": gamma, "beta": beta, "horizon": horizon, "h": h},
        "phase_at_cutoff_16": {
            "frequency_representation": frequency_phase,
            "time_representation": time_phase,
            "absolute_difference": representation_error,
            "comparison_tolerance": PHASE_TOL,
            "frequency_error_estimate": frequency_error,
            "outer_time_error_estimate": time_error,
        },
        "limiting_phase": limit_phase,
        "limiting_phase_error_estimate": limit_error,
        "limiting_witness_distance": float(abs(limit_coherence - markov_coherence) / 2.0),
        "finite_cutoffs": rows,
    }


def main():
    with warnings.catch_warnings():
        warnings.simplefilter("error", IntegrationWarning)
        report = {
            "versions": {
                "python": platform.python_version(),
                "numpy": np.__version__,
                "scipy": scipy.__version__,
            },
            "quadrature_absolute_tolerance": QUAD_ABS,
            "quadrature_relative_tolerance": QUAD_REL,
            "oscillator": oscillator_check(),
            "cutoff": cutoff_check(),
            "status": "passed",
        }
    print(json.dumps(report, indent=2, sort_keys=True, allow_nan=False))


if __name__ == "__main__":
    main()
