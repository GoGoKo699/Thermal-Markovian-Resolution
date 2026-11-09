# From quantum processes to thermal control resolution

In the specified pure-dephasing model, a qubit keeps its populations while its coherence decays as a real exponential. Knowing this full coherence multiplier for every waiting time determines its uncontrolled channel. A different experiment interrupts the evolution, stores information in a protected reference, and measures the two systems together. The question of this project is how accurately the same Markov description predicts those controlled experiments when only a limited number of contacts is available.

The distinction has a concrete instance below. Two models agree on every uncontrolled channel. With one contact halfway through the observation time, a specified binary measurement has probabilities about $`0.5354`$ and $`0.4646`$ in the two models. The complete contact law then asks both how such a discrepancy can be accumulated and how large any allowed experiment can make it.

## How this bridge connects to the milestone map

The [30-milestone map](milestones.md) gives the complete learning structure. M01–M14 establish the background and assemble the controlled-process question; M15–M30 develop the calibrated response, matching bounds and physical approximations.

| Part of this bridge | Milestone connection |
|---|---|
| Objects, preparation and allowed experiments | M01–M14 |
| The complete one-contact experiment | M01, M07, M11–M12 and M18, then M22–M23 |
| Calibration and the universal operational bound | M15–M21 |
| Matching contact scaling | M22–M24 and M28 |
| Physical approximation and the scope of the result | M25–M30 |

## Selected educational source

Simon Milz and Kavan Modi, *Quantum Stochastic Processes and Quantum non-Markovian Phenomena*, **PRX Quantum 2, 030201 (2021)**, [DOI: 10.1103/PRXQuantum.2.030201](https://doi.org/10.1103/PRXQuantum.2.030201). The selected version is **[arXiv:2012.01894v2](https://arxiv.org/abs/2012.01894v2)**, revised 10 May 2021. The [author PDF](https://arxiv.org/pdf/2012.01894v2) inspected for this bridge identifies itself as that version and has 69 pages. Page numbers below are its printed page numbers.

This is the project's one educational anchor. The research sources credited later supply attribution and technical dependencies.

### A short route through the source

| Location in version 2 | Connection to this project |
|---|---|
| §IV.C, p.26 | Channel generators and semigroups |
| §V.B, p.35, especially Eqs. (141)–(145) | Instruments: outcomes and state changes |
| §V.D, p.40 | Several intervention times |
| §V.D.6, p.46, Eqs. (189)–(190) | Testers, feedback, and reusable ancillas |
| §VI.A.1, p.51, Eqs. (204)–(206) | Markov processes as independent interval channels |
| §VI.A.2, p.53, Eqs. (208)–(214) | Divisible dephasing with intervention-visible memory |

The last example uses a Lorentzian environmental wavefunction. It is a conceptual comparison; the thermal oscillator model and quantitative contact law are derived in this repository.

## Translating the objects and assumptions

| Source notation | Project notation and role |
|---|---|
| $`S,E`$ | Probe $`S`$ and inaccessible bosonic bath; $`R`$ is a separate protected reference |
| $`\sigma_3`$ | $`Z`$, with eigenvalues $`+1,-1`$ |
| $`\mathcal E_{(t:s)}`$ | The comparison channel is $`\mathcal M_{t-s}`$ |
| $`\mathcal A_{x_j}`$ | An outcome map; $`\mathcal A_j`$ in the proof also retains its classical record |
| $`T_k`$ | A preassigned grid with at most $`N`$ interior contacts |
| $`\Upsilon_{T_k}`$ and tester elements | The bath process $`\mathcal P_\beta`$ and an accessible experiment $`\mathsf T`$ |

The dephasing convention also needs translation: the source's Eqs. (107) and (211) use $`e^{-\gamma_{\rm MM}t}`$; here the coherence multiplier is $`e^{-2\gamma t}`$. Matching these displayed decay rates means $`\gamma_{\rm MM}=2\gamma`$, without identifying the two microscopic models.

For the project, use units $`\hbar=k_B=1`$. The positive parameter $`\beta`$ is inverse temperature, and $`\gamma`$ sets the dephasing rate. The target generator is

```math
\mathcal L_\gamma(\rho)=\gamma(Z\rho Z-\rho),
\qquad
\mathcal M_t=e^{t\mathcal L_\gamma}.
```

It preserves populations in the $`Z`$ basis and multiplies each off-diagonal element by $`e^{-2\gamma t}`$. The statement that the actual uncontrolled channel equals $`\mathcal M_t`$ is imposed for **every** $`t\ge0`$. It is stronger than fitting finitely many decay data or even obtaining exact agreement on one finite time window. The [calibration proof](../science/calibration.md) makes this distinction explicit.

The probe has longitudinal coupling $`Z\otimes B`$ to a centered linear bosonic field. Oscillator frequencies are positive. Before each run, the bath is Gaussian and KMS at inverse temperature $`\beta`$ for its **free** Hamiltonian $`H_B`$, independently of the prepared probe and reference. This is a product preparation followed by interacting evolution. It is not equilibrium for the coupled Hamiltonian. The family of coupling spectra is calibrated separately at each temperature.

An allowed experiment chooses its contact times before the run. At those times it may use arbitrary finite-outcome instruments, keep every outcome, and choose later operations using earlier records. It may retain any finite protected quantum memory. Initial preparation and final joint measurement are free; each interior operation involving the probe counts as one contact. Outcome-dependent contact times, coherent control of those times, and continuous noncommuting probe driving are outside the theorem. These assumptions are specified in the [model](../science/model.md).

For the same experiment $`\mathsf T`$, compare its normalized accessible output states under the thermal process and the Markov process:

```math
d_N(\beta,\gamma,\tau)
=\sup_{\mathsf T:\,K\le N}
\frac12\left\|\rho_\beta^{\mathsf T}-\rho_{\rm M}^{\mathsf T}\right\|_1.
```

The trace norm sums a matrix's singular values. The half trace distance here equals the largest difference in the probability of one final binary event. The supremum includes the allowed fixed grid, preparation, memory, operations, and readout. All recorded branches count with their actual probabilities; a rare successful branch is not renormalized to probability one. This is a single-run comparison with a specified Markov process, rather than a minimization over every possible Markov model or a cost law for repeating an experiment.

## A complete experiment with one contact

Take

```math
\gamma=1,\qquad \beta=0.4,\qquad
\tau=1,\qquad h=\tau/2=0.5.
```

The parameters and the two models are known when choosing the experiment. The only interior contact will be at the fixed time $`h`$.

### Preparation and operation

Prepare the reference qubit in $`|+\rangle_R=(|0\rangle_R+|1\rangle_R)/\sqrt2`$ and the probe in $`|+z\rangle_S`$. At time $`h`$, apply

```math
V=|0\rangle\langle0|_R\otimes I_S
 +|1\rangle\langle1|_R\otimes X_S.
```

Here $`X_S`$ exchanges the two $`Z`$ eigenstates. This conditional operation is one contact. The reference does not interact with the bath during either waiting interval.

The two coherent reference branches give two conditional probe histories:

| Interval | Branch $`R=0`$: $`a(t)`$ | Branch $`R=1`$: $`b(t)`$ | What the branches do |
|---|---:|---:|---|
| $`0\lt t\lt h`$ | $`+1`$ | $`+1`$ | Apply the same force to the bath |
| $`h\lt t\lt\tau`$ | $`+1`$ | $`-1`$ | Acquire a relative phase and decay |

During the first interval the probe stays in one eigenstate, so its reduced state does not change. The bath nevertheless evolves under that common force. During the second interval the branches differ, allowing the final interference to read the earlier bath response. The protected reference retains the coherence needed to compare the branches.

### Computing the final coherence

For the calibrated model, the [exact Gaussian influence formula](../science/operational_bound.md#conditional-bath-histories) is

```math
F[a,b]=\exp\!\left[
-\frac\gamma2\int_0^\tau(a(t)-b(t))^2dt
+i\int_{0\lt s\lt t\lt\tau}
 (a(t)-b(t))(a(s)+b(s))\eta_\beta(t-s)\,ds\,dt
\right],
```

with positive-time response

```math
\eta_\beta(u)=\frac\gamma\beta
\mathrm{csch}\!\left(\frac{\pi u}{\beta}\right),
\qquad \mathrm{csch}x=\frac1{\sinh x}.
```

The two histories differ by two for time $`h=0.5`$, so the real exponent is

```math
-\frac12\cdot 2^2\cdot0.5=-1.
```

Their coherence modulus is therefore $`v=e^{-1}`$ in both models. The response phase is

```math
\begin{aligned}
\Phi
&=4\int_h^{2h}dt\int_0^h ds\,\eta_{0.4}(t-s)\\
&=4\int_0^h u\eta_{0.4}(u)\,du
 +4\int_h^{2h}(2h-u)\eta_{0.4}(u)\,du\\
&\approx0.3873488773.
\end{aligned}
```

The factor four is the product of the later history difference, two, and the earlier history sum, two. Every contribution is positive. The triangular integration weight vanishes at zero separation, making the integral finite despite $`\eta_\beta(u)\sim\gamma/(\pi u)`$ there. The numerical value is reproduced by the existing [witness verification](../verification/README.md#2-finite-cutoff-phase-in-two-representations).

At time $`\tau`$, introduce the two orthogonal joint states

```math
|e_0\rangle=|0\rangle_R|+z\rangle_S,
\qquad
|e_1\rangle=|1\rangle_R|-z\rangle_S.
```

Both outputs are supported on their span. In the ordered basis $`(|e_0\rangle,|e_1\rangle)`$,

```math
\rho_\beta=\frac12
\begin{pmatrix}
1&ve^{i\Phi}\\
ve^{-i\Phi}&1
\end{pmatrix},
\qquad
\rho_{\rm M}=\frac12
\begin{pmatrix}
1&v\\
v&1
\end{pmatrix}.
```

The populations and coherence magnitudes agree. The phase changes a measurable interference probability.

### An explicit binary readout

At the final time, measure the projector onto

```math
|\chi_+\rangle
=\frac{|e_0\rangle-i e^{-i\Phi/2}|e_1\rangle}{\sqrt2}.
```

The two effects are $`E_+=|\chi_+\rangle\langle\chi_+|`$ and $`E_-=I_{RS}-E_+`$. This is a joint readout on the probe and reference. Its dependence on the known phase is permitted. The final measurement is free, so it adds no interior contact.

Direct multiplication of these two-dimensional matrices gives

```math
\begin{aligned}
p_\beta(+)&=\frac{1+v\sin(\Phi/2)}2
             \approx0.5354021287,\\
p_{\rm M}(+)&=\frac{1-v\sin(\Phi/2)}2
             \approx0.4645978713.
\end{aligned}
```

Thus the final-event discrepancy is

```math
D=p_\beta(+)-p_{\rm M}(+)
=e^{-1}\sin(\Phi/2)
\approx0.0708042574.
```

This measurement is optimal for these two output states: the difference matrix has eigenvalues $`\pm D`$, and $`E_+`$ projects onto its positive eigenspace. Consequently $`D=\tfrac12\|\rho_\beta-\rho_{\rm M}\|_1`$. With equal model priors, guessing “thermal” on $`+`$ succeeds with probability $`(1+D)/2\approx0.5354021287`$.

This establishes $`d_1(0.4,1,1)\ge D`$. It does not establish that this is the globally best one-contact experiment. The resource account is exact: one reference qubit, one fixed interior contact, and one free final joint measurement. Reading only the reference in this construction discards the interference because the two final probe states are orthogonal.

## Why the free channel leaves this possibility open

Without a contact, the two longitudinal histories are constant. Their response factor contains

```math
(a-b)(a+b)=a^2-b^2=0.
```

The bath's antisymmetric response therefore drops out of the uncontrolled coherence. Free calibration fixes the symmetric fluctuations, which produce the exponential decay. An operation can instead create an earlier interval with nonzero history sum and a later interval with nonzero history difference. The product between these different intervals need not vanish; it is exactly four in the worked example.

Applying the calibrated channel independently to each interval assumes that the earlier bath change has no further effect. That is the Markov comparison being tested. Equality of all uninterrupted channels does not establish this stronger operational statement. In the example, the disagreement appears in a phase, even though each model predicts the same coherence magnitude. The [interpretation](../science/interpretation.md) explains the physical distinction and its scope.

## The proof steps supplied by this project

The example demonstrates an attainable discrepancy. Establishing a matching contact law also requires control of every permitted experiment. The following argument joins the thermal calculation to the operational framework.

### Exact calibration fixes the coupled spectrum

Let $`\mu(d\omega)=\coth(\beta\omega/2)J(d\omega)`$ be the positive symmetrized spectral measure. The [calibration theorem](../science/calibration.md#thermal-covariance-and-admissible-spectral-measures) permits measures with finite mass near zero and an integrable $`\omega^{-2}`$ weighted ultraviolet tail. These conditions allow white symmetrized noise while keeping integrated finite-interval variances finite.

The uncontrolled exponent is

```math
\Gamma(t)=4\int_0^\infty
\frac{1-\cos(\omega t)}{\omega^2}\,\mu(d\omega).
```

Requiring $`\Gamma(t)=2\gamma t`$ at all nonnegative times gives, by even extension and distributional Fourier uniqueness,

```math
\mu(d\omega)=\frac\gamma\pi d\omega,
\qquad
J_\beta(d\omega)=\frac\gamma\pi
\tanh\!\left(\frac{\beta\omega}{2}\right)d\omega.
```

KMS supplies the second equality: it relates the positive and negative frequency weights, hence relates fluctuations to response. The proof also shows that any admitted static Gaussian component must vanish. It identifies the coupled spectral measure, not a unique microscopic mode realization. Finite-window calibration has explicit counterexamples to this uniqueness; approximate calibration is a separate problem.

### A finite response moment controls each contact

The calibrated response is the $`\mathrm{csch}`$ kernel used above. Its unweighted integral diverges at zero, but

```math
\int_0^\infty u\eta_\beta(u)\,du=\frac{\gamma\beta}{4}.
```

For a contact at time $`t_c`$, every response pair crossing it has an earlier time $`s\lt t_c`$ and a later time $`t\gt t_c`$. At a separation $`u=t-s`$, the measure of these pairs is at most $`u`$. Hence

```math
\int_0^{t_c}ds\int_{t_c}^{\tau}dt\,\eta_\beta(t-s)
\le\frac{\gamma\beta}{4}.
```

Positivity lets the proof charge every inter-interval response pair to the contacts it crosses. At most $`N`$ contacts then give a coefficient budget $`S\le N\gamma\beta`$ after expanding the four signed history monomials in each response term.

### The coefficient bound must be promoted to a bound on complete experiments

A small phase in each matrix entry does not by itself bound the best protected-memory experiment. The [operational proof](../science/operational_bound.md#from-history-factors-to-circuit-insertions) supplies the missing step. A history sign becomes left or right multiplication by $`Z`$ at the correct place in the complete circuit. These multiplications have completely bounded trace norm one; so do the surrounding physical evolution and recorded instruments. The proof never moves an insertion through a noncommuting instrument.

Expanding the response exponential and summing its absolute coefficients therefore gives

```math
\frac12\|\rho_\beta^{\mathsf T}-\rho_{\rm M}^{\mathsf T}\|_1
\le\frac{e^S-1}{2}.
```

This estimate has no extra factor for memory size, histories, or outcome branches. Taking the supremum over allowed testers and using $`S\le N\gamma\beta`$ yields

```math
d_N\le\min\!\left\{1,\frac{e^{N\gamma\beta}-1}{2}\right\}
\le\min\{1,N\gamma\beta\}.
```

The complete-circuit argument is a substantive proof dependency. The educational framework explains the operational question; it does not replace this norm estimate.

### Coherent histories attain the matching order

At $`\tau=1/\gamma`$, divide the time into $`2m`$ equal intervals and apply the same reference-controlled flip at each of their $`2m-1`$ internal boundaries. One branch stays positive; the other alternates. Their difference is nonzero for exactly half the horizon, so the coherence modulus remains $`e^{-1}`$. Every contributing response phase has the same sign.

The [witness proof](../science/witness.md) chooses $`m`$ within the contact budget. It controls both small accumulated phase and the regime where enough contacts are available to reach a constant discrepancy. For large $`\gamma\beta`$, one contact suffices, and a monotone bound on its phase prevents wrapping. These are fixed schedules chosen from known parameters, not outcome-dependent times.

Together, the upper bound and witness give, for every finite $`\beta\gt0`$ and integer $`N\ge1`$,

```math
c\min\{1,N\gamma\beta\}
\le d_N(\beta,\gamma,1/\gamma)
\le\min\{1,N\gamma\beta\},
\qquad
c=\frac{e^{-1}}{4\pi\sinh\pi}
\approx0.0025349014.
```

The constant is conservative. One protected qubit suffices for the lower bound; the result does not prove that protected memory is necessary. With no interior contact, $`d_0=0`$.

For a **fixed** target discrepancy $`0\lt\delta\le c`$, the upper bound requires $`N\ge\delta/(\gamma\beta)`$. The lower bound guarantees that a budget

```math
N=\left\lceil\frac{\delta}{c\gamma\beta}\right\rceil
```

is sufficient. Thus as $`\gamma\beta\to0`$, the necessary and sufficient order is $`N=\Theta(1/(\gamma\beta))`$, with constants depending on the chosen target. At the fixed horizon, average contact spacing is of order $`\beta`$, or $`\hbar/(k_B T_{\rm bath})`$ with units restored. The range $`0\lt\delta\le c`$ is part of this guaranteed consequence; the theorem does not promise every target below one.

## Physical approximations and the meaning of the cutoff

Exact calibration uses an ultraviolet limit. For a finite cutoff, set

```math
J_{\beta,\Omega}(\omega)
=J_\beta(\omega)\mathbf1_{(0,\Omega]}(\omega).
```

The [regularization theorem](../science/regularization.md) constructs the limiting process from ordinary finite-cutoff Gaussian models and proves

```math
d_N(\mathcal P_{\beta,\Omega},\mathcal P_\beta;\tau)
\le\min\!\left\{1,
\frac{\exp\!\left(16\gamma(N+1)^2/(\pi\Omega)\right)-1}{2}
\right\}.
```

This is uniform over the specified fixed schedules, instruments, and finite protected memories. The uncontrolled exponent also satisfies

```math
0\le2\gamma t-\Gamma_\Omega(t)
\le\frac{8\gamma}{\pi\Omega}
\qquad(t\ge0).
```

Thus, for this explicit continuum cutoff family, increasing $`\Omega`$ makes all free channels arbitrarily accurate while preserving the limiting controlled discrepancy. This is a construction, not a lower bound on every approximately calibrated finite bath.

The same one-contact experiment illustrates the distinction. Its finite-cutoff coherence is

```math
\begin{aligned}
q_\Omega&=e^{-\Gamma_\Omega(h)+i\Phi_{1,\Omega}},\\
\Phi_{1,\Omega}
&=4\int_0^\Omega J_\beta(\omega)
\frac{2\sin(\omega h)-\sin(2\omega h)}{\omega^2}\,d\omega.
\end{aligned}
```

The optimized binary readout for those two output states has discrepancy $`|q_\Omega-e^{-1}|/2`$. The [existing calculation](../verification/README.md) gives about $`0.0709969675`$ at $`\Omega=256`$, close to the limiting $`0.0708042574`$. Here the readout can be chosen for the known finite-cutoff pair of states. The full complex coherence matters: at finite cutoff its modulus is not exactly $`e^{-1}`$. Hard-cutoff errors need not vary monotonically with $`\Omega`$.

Three different approximations must remain distinct. A **frequency cutoff** bounds each mode frequency. A **finite-mode approximation** replaces the spectral integral by finitely many positively weighted oscillators for a fixed finite observation problem. Neither step makes the oscillator Hilbert spaces finite-dimensional or bounds their excitation energies. A **Fock truncation**, such as the 40- and 60-level matrices in the verification script, is an additional numerical approximation used for a finite convention check. The project provides no optimized mode-count or Hilbert-dimension law, and the finite-mode statement does not assert uniform approximation for arbitrarily long times.

For finite $`\beta`$ and $`\Omega`$, the conditional Hamiltonians are semibounded; adding a common scalar shift makes them nonnegative without changing probabilities. The continuum thermal state is understood through its Gaussian KMS expectations or finite-mode Gibbs approximants. No trace-class continuum Gibbs density matrix or ordinary finite-variance white field at infinite cutoff is assumed. The cutoff and contact count also leave control work and occupation unbounded.

## Attribution and direct proof routes

The selected source supplies the operational foundations. The thermal contact law depends on additional research ingredients, with their roles separated in [Related work](../references/RELATED_WORK.md):

| Ingredient | Research dependency and project use |
|---|---|
| Exact Gaussian history influence | Feynman–Vernon's linear-environment method; the project gives its displacement-operator derivation in [operational_bound.md](../science/operational_bound.md). |
| Free semigroup with intervention-dependent phases | Lonigro–Chruściński, Proposition 3.2 and Eq. (67); this is an established mechanism, not a first counterexample claimed here. |
| Decay versus environmental response phase | Wang–Clerk's Gaussian spectroscopy formulas, including Eq. (12); the project uses this distinction in the protected-reference witness. |
| Bounds from integrated Gaussian covariance changes | Huang–Zhu–Park–Lin, Theorem 2.9 and the inserted-circuit argument near Eq. (2.46), with related bounds in Liu–Lu, Theorem 1; the project spells out the fixed-instrument norm estimate and ultraviolet limit. |
| Contact-boundary geometry | The pinned Autonomous-Markovian-Noise comparison credits the earlier boundary-moment method; the present response is imaginary and KMS constrained, so it is not a direct classical-covariance substitution. |
| Spectral and Hamiltonian foundations | Distributional Fourier uniqueness, equivalently Lévy–Khintchine uniqueness, supports [calibration](../science/calibration.md); the KLMN form argument supports [regularization](../science/regularization.md#2-finite-cutoff-hamiltonians-are-semibounded). |

The project supplies the exact all-time calibrated thermal family, the complete fixed-contact operational bound, the matching witness with its all-temperature schedule choice, and the quantified cutoff approximation. Milz–Modi is not cited as proving those results.

For the full scientific route, read [the model](../science/model.md), [spectral calibration](../science/calibration.md), [the operational proof](../science/operational_bound.md), [the witness](../science/witness.md), and [regularization](../science/regularization.md). The [interpretation](../science/interpretation.md) states the resulting contact threshold and its limits. The [verification guide](../verification/README.md) documents the existing independent oscillator and integral checks, and separates those finite checks from the analytical theorems.
