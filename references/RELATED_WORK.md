# Related work and attribution

The question studied here is quantitative: when an exactly calibrated thermal dephasing bath is tested through a limited number of contacts, how far can its full controlled process depart from the corresponding Markov process?

The [calibration theorem](../science/calibration.md) fixes the spectrum within the stated stationary linear Gaussian/KMS class. The [operational upper bound](../science/operational_bound.md) and [explicit witness](../science/witness.md) give the matching order

```math
d_N=\Theta\!\left(\min\{1,N\gamma\beta\}\right),
\qquad
\tau=\gamma^{-1}.
```

The [regularization theorem](../science/regularization.md) supplies physical finite-cutoff approximants. The comparison below identifies the established phenomena, mathematical methods, and operational concepts used in proving that statement. Bibliographic entries are collected in [references.bib](references.bib).

## 1. Free semigroup dynamics does not determine multitime dynamics

The distinction between reduced channels and a complete process under interventions is established. [Pollock et al., Physical Review Letters 120, 040405 (2018)](https://doi.org/10.1103/PhysRevLett.120.040405), formulate an operational Markov condition in terms of all detectable memory effects. [Milz and Modi, PRX Quantum 2, 030201 (2021)](https://doi.org/10.1103/PRXQuantum.2.030201), give a detailed account of quantum stochastic processes and the quantum-comb framework. Protected-memory testers and operational process distances belong to this existing framework.

The closest exact dephasing comparison is [Lonigro and Chruściński, Journal of Physics A 55, 225308 (2022)](https://doi.org/10.1088/1751-8121/ac6a2d), [full preprint](https://arxiv.org/pdf/2202.11056). Proposition 2.2 gives a hierarchy characterizing regression under arbitrary interventions. Proposition 3.2 distinguishes a flat spectrum on the full frequency line from one restricted to positive frequencies. In the latter, the vacuum model has semigroup dephasing magnitudes but additional history-dependent phases; Eq. (67) displays a two-interval example.

That exact hidden-phase mechanism is an antecedent of the present construction. This repository does not claim a first example of a semigroup with failed regression. Its additional task is to resolve the finite-temperature dependence quantitatively, optimize over the stated contact-budget class, and show a matching bound with finite-cutoff approximants. Phase constants here follow the explicit covariance convention and independent Weyl calculation in the scientific pages.

## 2. Thermal regression failure and controlled response phases

Thermal incompatibilities with regression are also established. [Talkner, Annals of Physics 167, 390–436 (1986)](https://doi.org/10.1016/0003-4916(86)90207-1), connects the regression hypothesis in an equilibrium formulation with KMS and fluctuation-dissipation constraints. That equilibrium setting differs from the product preparation used here. The general conflict between imposing memoryless regression and retaining a thermal quantum response is not a new claim of this work.

[Wang and Clerk, Nature Communications 12, 6528 (2021)](https://doi.org/10.1038/s41467-021-26868-7), [full preprint](https://arxiv.org/pdf/2104.02047), analyze intrinsic and induced quenches in qubit noise spectroscopy. Their Gaussian formulas, including Eq. (12), separate coherence decay controlled by symmetrized fluctuations from a phase controlled by environmental response. They use this phase for spectral information and thermometry, and discuss deliberately modulated quenches.

The present witness uses that established physical distinction. A protected qubit stores coherence while the probe branches alternate between equal and unequal longitudinal histories. The purpose of this schedule is to attain the contact-budget lower bound while keeping the white-noise decoherence fixed. It is not a claim of a new response-sensing principle or first quench thermometry.

At each inverse temperature, the coupling spectrum is calibrated anew. The statement therefore compares baths with equal free dephasing laws, rather than the temperature dependence of one fixed spectral density.

## 3. Operational regression errors and higher temporal orders

[Luppi, Benedetti and Smirne, Physical Review A 114, 052204 (2026)](https://doi.org/10.1103/ssf1-j2j8), [published full text](https://journals.aps.org/pra/pdf/10.1103/ssf1-j2j8), decompose the two-time propagator into a regression term and a correlation correction, Eq. (22), and measure fixed-protocol discrepancy by Kolmogorov distance, Eq. (28). They develop a weak-coupling correction and benchmark selected measurement protocols in a transverse spin-boson setting.

Their published Section IV.D proves exact QRT agreement for a selected two-time measurement sequence using parity, while an inserted intermediate measurement reveals a three-time discrepancy. The conclusion explicitly identifies optimization over possibly ancilla-assisted testers as the complementary operational process distance. Both exact lower-order blindness and that optimization framework are therefore prior concepts.

The present theorem addresses a different quantitative question: a matching law for all contact budgets in an exactly calibrated Gaussian/KMS dephasing class. Luppi et al. do not establish this temperature-dependent contact law. Their Lorentzian model, approximate narrow-linewidth pseudomode correspondence, and fixed-coupling temperature scans also differ from the calibrated spectral family considered here.

## 4. Gaussian perturbation bounds and the insertion method

The influence-functional treatment of a linear Gaussian environment is classical open-systems machinery. [Feynman and Vernon, Annals of Physics 24, 118–173 (1963)](https://doi.org/10.1016/0003-4916(63)90068-X), provide the foundational linear-environment construction.

[Mascherpa et al., Physical Review Letters 118, 100401 (2017)](https://doi.org/10.1103/PhysRevLett.118.100401), [full preprint](https://arxiv.org/pdf/1611.03377), bound errors in spin-boson observables from spectral-density variations. This is a direct antecedent for controlling output errors through integrated changes in bath correlations.

[Liu and Lu, Quantum 9, 1896 (2025)](https://doi.org/10.22331/q-2025-10-28-1896), [full preprint, version 3](https://arxiv.org/html/2408.04009v3), give a rigorous diagrammatic/combinatorial justification of this type of bound. Their Theorem 1, Eq. (23), has exponential dependence on an integrated covariance perturbation.

[Huang, Zhu, Park and Lin, arXiv:2411.08741, version 2](https://arxiv.org/html/2411.08741v2), treat Gaussian environments with a superoperator formalism, including nonstationary covariance functions. Theorem 2.9 and the contractive inserted-circuit argument around Lemma 2.11 are especially close to the norm estimate used here.

Accordingly, the present exponential comparison bound is a specialization of established Gaussian perturbation methods. The proof in [operational_bound.md](../science/operational_bound.md) spells out the history-to-circuit correspondence for arbitrary recorded instruments and protected memory at preassigned times. The proof in [regularization.md](../science/regularization.md) controls integrated coefficients before taking the singular ultraviolet limit. Neither an entrywise influence estimate nor a raw Choi-matrix norm is used as a substitute for the operational norm bound.

## 5. Matching Gaussian bath correlations at multiple times

[Smirne, Tamascelli, Lim, Plenio and Huelga, Open Systems & Information Dynamics 29, 2250019 (2022)](https://doi.org/10.1142/S1230161222500196), [full preprint, version 2](https://arxiv.org/pdf/2209.00293v2), establish equivalence of multitime expectation values when the corresponding Gaussian bosonic interaction operators have matching first and second correlation functions.

This equivalence explains why bath covariance data are sufficient to determine the controlled Gaussian process. The present comparison deliberately matches only the symmetrized spectrum, hence all uncontrolled qubit dephasing channels. The antisymmetric response remains different. Matching free reduced channels is therefore a weaker condition than the bath-correlation matching required by that equivalence theorem.

## 6. Closely related thermal two-time calculations

[Ban, Physical Review A 96, 042111 (2017)](https://doi.org/10.1103/PhysRevA.96.042111), studies two-operation correlation functions for an open system coupled to a thermal reservoir. The published abstract describes projection-operator expressions through second order, finite-correlation-time corrections to regression, and comparisons with exact pure-dephasing and linear-dissipative calculations. It has an [erratum, Physical Review A 97, 069901 (2018)](https://doi.org/10.1103/PhysRevA.97.069901).

[Ban, Kitajima and Shibata, Physical Review A 97, 052101 (2018)](https://doi.org/10.1103/PhysRevA.97.052101), describe an exact Gaussian-reservoir two-time formula and an expansion in the reservoir correlation time. Their abstract identifies the regression expression as the lowest-order term.

These are relevant thermal-regression antecedents. The source comparison here uses their publisher abstracts and bibliographic metadata; the full original papers and erratum were not accessible from the public locations checked. No claim is made about the erratum's detailed corrections, or about the absence of a particular formula from unread sections. The full-text comparisons in Sections 1–5 provide the more detailed attribution for the methods used here.

## 7. Relation to companion technical repositories

These comparisons concern the linked technical statements, not a claim that the repositories are peer-reviewed publications.

### Autonomous-Markovian-Noise

At revision [3d743d7a740fff773b9b95a4bbc4f3a2afcc3785](https://github.com/GoGoKo699/Autonomous-Markovian-Noise/tree/3d743d7a740fff773b9b95a4bbc4f3a2afcc3785), [science/adaptive_comparison.md](https://github.com/GoGoKo699/Autonomous-Markovian-Noise/blob/3d743d7a740fff773b9b95a4bbc4f3a2afcc3785/science/adaptive_comparison.md) proves a contact bound from the first moment of a real, even, nonnegative classical Gaussian covariance:

```math
d_N\le(2N+1)\mu,
\qquad
\mu=\int |u|K(u)\,du.
```

Its scalar boundary-crossing estimate is the geometric antecedent of the first-response-moment bound used here. It also handles classically adaptive timing, beyond the present theorem's timing class.

The substitution $`K\mapsto\eta_\beta`$ is not an instance of that proposition: $`\eta_\beta`$ is the positive-time part of an odd imaginary response kernel, not a real classical covariance. The [finite-bath construction](https://github.com/GoGoKo699/Autonomous-Markovian-Noise/blob/3d743d7a740fff773b9b95a4bbc4f3a2afcc3785/science/finite_bath.md) uses strongly commuting fields and a stationary nonthermal signed-frequency reference. Here KMS fixes a noncommuting response that survives exact free calibration. Contact counting and the boundary-moment geometry are shared; the thermal constraint and resulting floor are different.

### Markovian-Resolution-Limit

At revision [b4af5cfb7a86165f29d9cf1e9adcb74f5fe91a8b](https://github.com/GoGoKo699/Markovian-Resolution-Limit/tree/b4af5cfb7a86165f29d9cf1e9adcb74f5fe91a8b), [science/intervention_bounds.md](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/b4af5cfb7a86165f29d9cf1e9adcb74f5fe91a8b/science/intervention_bounds.md) supplies bounded-action Dyson estimates and contact-weighted cell comparisons. The matching resolution law uses a bounded-interaction survival obstruction, with a finite-cell construction for the converse; [science/dissipators.md](https://github.com/GoGoKo699/Markovian-Resolution-Limit/blob/b4af5cfb7a86165f29d9cf1e9adcb74f5fe91a8b/science/dissipators.md) gives the general dissipative statement.

That interaction-strength bound and the present thermal-response bound have different assumptions. The present model allows unbounded oscillator energies and does not impose a coupling-norm cap. Its parameter $`\Omega`$ bounds mode frequencies, not the spectral diameter of the complete oscillator Hamiltonian. The shared operational architecture is credited without identifying the two physical restrictions.

## 8. Scope of the quantitative result

The contribution developed here is the matched contact-temperature law after imposing exact all-time free calibration within the specified Gaussian/KMS class, together with an explicit witness and controlled cutoff approximation. The following distinctions are essential:

- The qualitative failure of regression, the response phase, the process-tensor viewpoint, Gaussian stability, and boundary-moment contact accounting have the antecedents above.
- The optimization is over protected-memory testers with preassigned contact times. Adaptive operations at those times are allowed; adaptive timing is not established.
- Exact all-time calibration determines the spectral family under the admissibility assumptions in [calibration.md](../science/calibration.md). Finite-window calibration does not supply the same uniqueness statement.
- The finite-cutoff theorem constructs approximants retaining the limiting thermal discrepancy. It is not a minimax lower bound over all approximately calibrated finite baths.
- No bound on control work, occupation, bath Hilbert-space dimension, or optimized mode count is part of the theorem.

The spectral uniqueness proof uses the standard uniqueness of the Lévy–Khintchine triplet; an accessible statement is [Pitman's Probability Theory lecture 26, Theorem 1.6](https://www.stat.berkeley.edu/users/pitman/s205s03/levy.pdf). This mathematical input is separate from the operational law.

### Source-comparison record

The relevant theorem/proof passages of Lonigro–Chruściński, Wang–Clerk, Liu–Lu, Huang et al., and Smirne et al. were read in the linked author versions. The Luppi et al. comparison uses the published body, including its higher-order section and conclusion. Talkner and the Ban papers are used only to the extent supported by their accessible abstracts/metadata. The companion comparisons use the pinned files linked above. The source record was checked on 9 November 2026 and is a bounded comparison, not a certification of exhaustive priority.
