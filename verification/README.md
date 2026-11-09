# Reproducing the witness convention checks

These small deterministic checks address two concrete failure modes: an incorrect phase sign or numerical factor in the influence functional, and a mismatch between the finite-cutoff and limiting covariance conventions. The analytical [witness proof](../science/witness.md) and [regularization bounds](../science/regularization.md) carry the uniform claims.

## Run

Use Python 3.12 and install the two pinned dependencies:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_witness.py
```

The reference environment is Python 3.12.14, NumPy 2.3.5, and SciPy 1.17.0. The script uses no random inputs or network access. It prints a compact JSON report and exits nonzero if a comparison fails or numerical integration raises an `IntegrationWarning`. It does not create or overwrite files.

## 1. Independent finite-oscillator evolution

For one mode, construct the matrices

```math
H_\pm=\omega a^\dagger a\pm g(a+a^\dagger)
```

and a truncated thermal density matrix. The parameters are $`\omega=1`$, $`g=0.3`$, $`\beta=1`$, and $`h=0.4`$. Direct matrix exponentials produce the two histories

```math
U_0=e^{-ihH_+}e^{-ihH_+},
\qquad
U_1=e^{-ihH_-}e^{-ihH_+}.
```

The trace $`\mathrm{Tr}(U_0\rho_\beta U_1^\dagger)`$ is compared with the exact oscillator influence factor

```math
\exp\left[
-\frac{4g^2}{\omega^2}\coth\left(\frac{\beta\omega}{2}\right)
(1-\cos\omega h)
+i\frac{4g^2}{\omega^2}(2\sin\omega h-\sin2\omega h)
\right].
```

The expected phase is approximately $`0.02213301373840017`$. Both the 60-level error against this expression and the change from 40 to 60 levels must be below $`2\times10^{-11}`$. The matrices do not implement the influence formula, so the comparison checks the phase factor, sign, operator ordering, and real exponent independently. Two cutoffs are a stability check at these parameters, not a rigorous bound on every Fock truncation.

## 2. Finite-cutoff phase in two representations

Set $`\gamma=1`$, $`\beta=0.4`$, $`\tau=1`$, and $`h=1/2`$. At $`\Omega=16`$, compare the frequency integral

```math
\Phi_{1,\Omega}
=4\int_0^\Omega J_\beta(\omega)
\frac{2\sin\omega h-\sin2\omega h}{\omega^2}\,d\omega
```

with the independently nested time-domain calculation

```math
4\int_0^h u\eta_{\beta,\Omega}(u)\,du
+4\int_h^{2h}(2h-u)\eta_{\beta,\Omega}(u)\,du,
\qquad
\eta_{\beta,\Omega}(u)
=\int_0^\Omega J_\beta(\omega)\sin\omega u\,d\omega.
```

The absolute difference must be below $`2\times10^{-8}`$. Each quadrature uses absolute and relative tolerance $`10^{-11}`$. The nested integration's reported error estimate is not a certified enclosure of the whole calculation; the explicit cross-representation tolerance is the acceptance check.

The script also reports the phase, modulus, and final-event discrepancy at $`\Omega=16,64,256`$, together with the limiting $`\mathrm{csch}`$-kernel answer. It uses the full complex coherence at finite cutoff: its modulus is not exactly $`e^{-1}`$. Hard-cutoff errors need not decrease monotonically, so monotonic convergence is not a test condition. The free-channel exponent deficit at the horizon is checked against the analytical bound $`8\gamma/(\pi\Omega)`$.

The limiting phase is approximately $`0.3873488773`$ and the limiting witness discrepancy is $`0.0708042574`$. The reference calculation gives the following rounded values. All distances are half trace distances of the two-dimensional witness outputs.

| Cutoff $`\Omega`$ | Distance to Markov output | Distance to limiting thermal output | Free exponent deficit at $`\tau=1`$ |
|---:|---:|---:|---:|
| 16 | 0.0748105590 | 0.0171643957 | 0.0787470342 |
| 64 | 0.0714498297 | 0.0037580472 | 0.0201761452 |
| 256 | 0.0709969675 | 0.0009224248 | 0.0049541871 |

In the reference environment, the finite-oscillator coherence error was below $`4\times10^{-16}`$ and the two finite-cutoff phase representations differed by less than $`3\times10^{-16}`$. These observed errors are smaller than the acceptance tolerances; bit-for-bit equality across numerical-library builds is not required.

## What the checks establish

Passing checks support the stated numerical conventions at the displayed finite parameters and guard against normalization or cutoff implementation errors. They do not prove the operational upper bound, uniformity in contact number or temperature, positivity of the limiting process, the continuum Hamiltonian construction, or convergence rates beyond the analytical bounds. The three displayed cutoffs are a reproducible illustration, not a parameter sweep or a substitute for those proofs.
