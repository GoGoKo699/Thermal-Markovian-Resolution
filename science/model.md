# The model and the thermal contact law

An uncontrolled decay curve describes the state at one time. A controlled experiment also probes how the environment responds to earlier operations. This project quantifies the difference for a precisely calibrated thermal dephasing model: every uncontrolled channel is a Markov semigroup, while sufficiently many interventions reveal memory.

The distinction itself is established in quantum regression and quantum noise spectroscopy. The result here is a matching bound on the largest discrepancy attainable with a specified number of contacts, together with physical finite-cutoff approximants. The [related-work account](../references/RELATED_WORK.md) identifies the inherited mechanisms and methods.

## 1. Probe, bath and calibration

Use units $`\hbar=k_B=1`$. A qubit $`S`$ couples longitudinally to a bosonic bath:

```math
H=I_S\otimes H_B+Z\otimes B,
\qquad
H_B=\int_0^\infty\omega b_\omega^\dagger b_\omega\,d\omega.
```

The field $`B`$ is linear in the creation and annihilation operators. Its mean vanishes in a stationary Gaussian KMS state of the **free** bath Hamiltonian at a finite inverse temperature $`0\lt\beta\lt\infty`$. Initially the probe and any protected memory are independent of the bath. This is a product preparation followed by the coupled dynamics, rather than a global equilibrium state of $`H`$.

The target channel semigroup is

```math
\mathcal M_t=e^{t\mathcal L_\gamma},
\qquad
\mathcal L_\gamma(\rho)=\gamma(Z\rho Z-\rho),
\qquad \gamma\gt0.
```

Its off-diagonal matrix elements decay as $`e^{-2\gamma t}`$. A known commuting probe Hamiltonian can be removed by a rotating frame; the target displayed here has no coherent rotation.

The exact calibration condition requires the uncontrolled reduced channel to equal $`\mathcal M_t`$ for **every** $`t\ge0`$. The [calibration theorem](calibration.md) states the admissible spectral-measure condition and proves that this forces

```math
J_\beta(\omega)=\frac{\gamma}{\pi}\tanh\!\left(\frac{\beta\omega}{2}\right),
\qquad \omega\gt0.
```

Thus the symmetrized spectrum is white. The unsymmetrized correlation, in the convention $`C(t)=\langle B(t)B(0)\rangle`$, retains a response:

```math
\mathrm{Re}C(t)=\gamma\delta(t),
\qquad
\eta_\beta(t):=-\mathrm{Im}C(t)
=\frac{\gamma}{\beta}\mathrm{csch}\!\left(\frac{\pi t}{\beta}\right)
\quad(t\gt0).
```

Exact calibration is an ultraviolet limit, not an assertion of a finite-variance white field operator. The [operational construction](operational_bound.md) defines its finite-contact processes as limits of conventional cutoff models. Spectra at different temperatures are separately calibrated; the formula does not describe heating one fixed coupling spectrum.

## 2. What counts as a controlled experiment

Fix an observation horizon $`\tau`$. An admissible tester chooses a deterministic grid

```math
0=t_0\lt t_1\lt\cdots\lt t_K\lt t_{K+1}=\tau,
\qquad K\le N.
```

It prepares an arbitrary state of $`S`$ and a protected memory $`R`$ of any finite dimension. At each interior grid point it applies an arbitrary finite-outcome quantum instrument to $`SR`$, keeps the classical outcomes, and may choose the operation using earlier outcomes. Such a complete recorded instrument is a CPTP map on the enlarged accessible state. Protected-memory-only operations may be absorbed into these maps because they commute with the probe–bath evolution between contacts.

Every interior operation involving the probe counts as one contact. Consecutive operations at the same time can be combined into one instrument. Initial preparation and final joint readout are free. The budget concerns one run over the fixed horizon. Independent repetition of entire runs is a separate resource.

The grid is fixed before the run. Outcome-dependent operations are allowed; outcome-dependent contact times and coherent control of contact times are outside the theorem. The probe has no additional noncommuting continuous drive between contacts. The bath is inaccessible to the tester.

For a tester $`\mathsf T`$, let $`\rho_\beta^{\mathsf T}`$ and $`\rho_{\rm M}^{\mathsf T}`$ be its accessible final states, including retained classical records, under the thermal process and the Markov process. In the latter, apply $`\mathcal M_{t_{j+1}-t_j}\otimes\mathrm{id}_R`$ between the same interventions. Define

```math
d_N(\beta,\gamma,\tau)
=\sup_{\mathsf T:\,K\le N}
\frac12\left\|\rho_\beta^{\mathsf T}-\rho_{\rm M}^{\mathsf T}\right\|_1.
```

The supremum includes the grid, initial state, memory dimension, instruments and final readout. Half trace distance is the largest difference of unconditional probabilities of a final binary event. With equal prior probabilities for the two models, the optimal discrimination success probability is $`(1+d_N)/2`$. A heralding event may be included in the output, but the definition does not renormalize by its success probability. Independent classical mixtures of fixed-grid testers obey the same upper bound by convexity.

## 3. Main theorem

**Thermal contact law.** Under the preceding assumptions, at $`\tau=1/\gamma`$ and for every integer $`N\ge1`$,

```math
\boxed{
c\min\{1,N\gamma\beta\}
\le d_N(\beta,\gamma,1/\gamma)
\le\min\{1,N\gamma\beta\},
\qquad
c=\frac{e^{-1}}{4\pi\sinh\pi}.
}
```

The constant is independent of temperature, contact number and protected-memory size. With no interior contact, exact calibration gives $`d_0=0`$. The lower bound is attained in order by a tester with one protected qubit; this is a sufficiency statement, not a proof that protected memory is necessary.

The [upper proof](operational_bound.md) first establishes

```math
d_N\le\min\!\left\{1,\frac{e^{N\gamma\beta}-1}{2}\right\}.
```

It uses the exact Gaussian influence functional, a circuit insertion estimate, and the positive response moment $`\int_0^\infty u\eta_\beta(u)\,du=\gamma\beta/4`$. No factor depending on the number of histories or memory dimension enters this estimate. The [witness proof](witness.md) gives a conditional alternating path whose response contributions have one sign, with a schedule choice that avoids phase wrapping in every temperature regime.

The statement optimizes over testers for a fixed process selected by exact calibration. It is not a minimization over all thermal baths or a certification theorem based on finitely many measured decay values.

## 4. Physical cutoff consequence

Let $`\mathcal P_\Omega`$ be the process with $`J_{\beta,\Omega}=J_\beta\mathbf1_{(0,\Omega]}`$, and let $`\mathcal P_\infty`$ denote the calibrated limit. Write $`d_N(\mathcal P,\mathcal Q;\tau)`$ for the same tester distance between two processes. The [regularization theorem](regularization.md) proves, uniformly over fixed grids and protected-memory dimension,

```math
d_N(\mathcal P_\Omega,\mathcal P_\infty;\tau)
\le\varepsilon_{N,\Omega},
\qquad
\varepsilon_{N,\Omega}
=\min\!\left\{1,
\frac{\exp\!\left(16\gamma(N+1)^2/(\pi\Omega)\right)-1}{2}
\right\}.
```

At the main theorem's horizon, the triangle inequality gives

```math
\max\!\left\{0,c\min\{1,N\gamma\beta\}-\varepsilon_{N,\Omega}\right\}
\le d_N(\mathcal P_\Omega,\mathcal M;1/\gamma)
\le\min\!\left\{1,N\gamma\beta+\varepsilon_{N,\Omega}\right\}.
```

Meanwhile the uncontrolled coherence exponent differs from $`2\gamma t`$ by at most $`8\gamma/(\pi\Omega)`$, uniformly in $`t\ge0`$. For fixed $`N,\beta,\gamma`$, increasing $`\Omega`$ therefore makes free calibration arbitrarily accurate while retaining the thermal controlled discrepancy. The constants give sufficient cutoff requirements; bandwidth optimality is not claimed.

## 5. Resources and limiting order

| Quantity or assumption | Role in the theorem |
|---|---|
| Interior probe contacts | Charged resource; at most N per run |
| Observation time | Fixed at tau = 1/gamma for the matching law |
| Protected memory | Arbitrary finite dimension; one qubit suffices for the lower bound |
| Classical records and feedback operations | Included at the preassigned contacts |
| Contact duration and control work | Instantaneous ideal contacts; no work budget |
| Bath spectrum and temperature | KMS and exact all-time calibration fix the coupled spectrum |
| Ultraviolet cutoff | Removed at fixed temperature, contact budget and horizon; explicit error bound provided |
| Finite mode discretization | Approximation exists as described in regularization; each oscillator retains its untruncated Hilbert space |

A temperature-dependent spectrum, free-bath product preparation and all-time calibration are part of the result. The cutoff bounds oscillator mode frequencies, not the spectral diameter of the full bath Hamiltonian or the interaction norm. At finite cutoff the Hamiltonians are semibounded, but their energy shift and contact work need not remain bounded as the cutoff grows. The [interpretation](interpretation.md) explains why the resulting operational threshold differs from a mode-frequency cutoff or bounded-interaction obstruction.

## Reading route

Read [calibration](calibration.md) for the exact class and its finite-window boundary; [operational bound](operational_bound.md) for the Gaussian process and complete tester estimate; [witness](witness.md) for the matching construction; and [regularization](regularization.md) for the physical approximants. The [verification guide](../verification/README.md) describes finite calculations that check conventions and approximation formulas. The analytical proofs establish the general theorem.
