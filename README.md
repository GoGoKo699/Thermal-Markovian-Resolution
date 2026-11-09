# Thermal Markovian Resolution

**How many interventions reveal the memory of a thermal environment whose uncontrolled channels exactly reproduce a Markov dephasing semigroup?** This project gives a matching contact–temperature law for a stationary Gaussian bosonic bath with linear longitudinal coupling, together with physical finite-cutoff approximations.

The bath starts thermal for its free Hamiltonian and independently of the probe. Exact calibration at every time fixes its coupled spectrum. Over a horizon $`\tau=1/\gamma`$, the largest final-event probability discrepancy from the Markov process obeys

```math
\boxed{
c\min\{1,N\gamma\beta\}
\le d_N\le\min\{1,N\gamma\beta\},
\qquad
c=\frac{e^{-1}}{4\pi\sinh\pi}.
}
```

Here $`\mathcal L_\gamma(\rho)=\gamma(Z\rho Z-\rho)`$, $`\beta`$ is inverse temperature in units $`\hbar=k_B=1`$, and $`N\ge1`$ counts interior probe contacts. The distance optimizes over **preassigned contact times**, protected quantum memories of arbitrary finite dimension, instruments, retained outcomes and feedback operations at those times. One protected qubit suffices to attain the order. With no intervention, the uncontrolled channels agree exactly and $`d_0=0`$.

The qualitative distinction between a free semigroup and a process with memory, the response-phase mechanism, and Gaussian perturbation methods are [established ingredients](references/RELATED_WORK.md). The result here is the matched operational contact law for the calibrated thermal class. When $`\gamma\beta\ll1`$, obtaining any fixed discrepancy between zero and $`c`$ requires and permits order $`1/(\gamma\beta)`$ contacts.

## Read the science

Start with the [model and exact claims](science/model.md). The proof route follows calibration, the operational upper bound, the matching witness and physical regularization.

| Question | Authoritative account |
|---|---|
| What is calibrated, and what can the tester do? | [Model, resources and main theorem](science/model.md) |
| Why does all-time calibration fix the spectrum? | [Spectral uniqueness and the finite-window boundary](science/calibration.md) |
| Why does the upper bound allow arbitrary protected memory? | [Gaussian influence and the complete operational bound](science/operational_bound.md) |
| Which experiment reaches the contact scaling? | [Protected-reference witness](science/witness.md) |
| How is the singular white model approached physically? | [Cutoff theorem and finite-mode approximation](science/regularization.md) |
| What changes in the validity of a controlled Markov model? | [Physical interpretation](science/interpretation.md) |
| Which mechanisms and methods are inherited? | [Related work](references/RELATED_WORK.md) and [bibliography](references/references.bib) |
| Which finite calculations can be reproduced? | [Verification guide](verification/README.md) |

The [LLM reading guide](llms.txt) maps questions to these scientific sources.

## Learning route

The selected educational source is **Milz and Modi, *Quantum Stochastic Processes and Quantum non-Markovian Phenomena* (2021), arXiv version 2**. The [source bridge](learning/milz_modi_bridge.md) translates its operational framework into this thermal model and works through one complete contact experiment, including the final binary measurement.

The [30-milestone map](learning/milestones.md) develops 14 background milestones and 16 milestones through the result. It connects the quantum-process foundations to the microscopic thermal calculation, then joins the universal upper bound, attaining witness and physical approximation. The map ends each phase with a synthesis of the full argument.

## Physical approximation

Exact free-semigroup behavior requires an ultraviolet process limit. For its explicit positive-frequency cutoff family, the free-channel error tends to zero uniformly in time as the mode-frequency cutoff grows. An explicit process bound also controls every fixed contact budget. Consequently the finite-cutoff family retains a nonzero controlled discrepancy while its free-channel calibration becomes arbitrarily accurate.

At finite cutoff and temperature, the Hamiltonians are semibounded. Finite-mode approximations with normalized thermal density matrices reproduce the process on a fixed observation horizon. A mode-frequency cutoff is not a bound on the full oscillator Hamiltonian or interaction norm, and finite modes still have infinite-dimensional Hilbert spaces.

## Reproduce the convention checks

From the repository root, run:

```bash
python -m pip install -r verification/requirements.txt
python verification/check_witness.py
```

The deterministic checks compare direct oscillator-matrix evolution with the Gaussian influence factor and compare frequency- and time-domain cutoff phase integrals. They check phase normalization, history ordering and approximation conventions. The analytical proofs establish the bounds uniformly in contact number, temperature and protected-memory size.

## Scope

Calibration is exact **for all times** in the limiting process. The spectrum changes with temperature to preserve the same target rate. The initial thermal state belongs to the free bath Hamiltonian; it is not a globally interacting Gibbs preparation. Contact times are preassigned and operations are instantaneous. Control work, bath preparation cost and optimal mode or occupation resources are uncharged.

The finite-cutoff consequence concerns approximants of the specified calibrated class. A finite-window or approximate experimental semigroup fit alone does not imply the same theorem. The precise distinctions and limiting order are part of the [model](science/model.md#5-resources-and-limiting-order).

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
