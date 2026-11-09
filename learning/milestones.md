# Thirty milestones for the thermal contact law

The scientific question is how many interventions can reveal the memory of a thermal environment when every uncontrolled channel agrees exactly with a dephasing semigroup. The answer concerns a particular calibrated Gaussian thermal class, a stated family of experiments, and a controlled limit of physical approximations.

The map has **14 background/preliminaries milestones, M01–M14**, followed by **16 narrative/innovation milestones, M15–M30**. The background allocation connects two bodies of knowledge that the argument needs together: quantum processes with interventions, and Gaussian thermal dephasing. The narrative then assembles spectral identification, an upper bound valid for every permitted tester, an attaining witness, and physical approximations. It follows the scientific dependencies rather than the order of a textbook or every technical lemma.

Within the background phase, individual states, channels, bath variables and operations become the complete operational problem at M14. Within the narrative phase, the calibrated response and its local effects become a resource law with an explicit realization and carefully delimited meaning at M28–M30. **M14 and M30 are the phase syntheses.** Specialist calculations remain in the linked proof pages; these targets organize global understanding rather than promise coverage of every detail.

## Sources and notation

The one educational anchor is Simon Milz and Kavan Modi, *Quantum Stochastic Processes and Quantum non-Markovian Phenomena*, PRX Quantum 2, 030201 (2021), [arXiv:2012.01894v2](https://arxiv.org/abs/2012.01894v2). All anchor section and page references below use the **69-page version-2 preprint**, verified in the [open PDF](https://arxiv.org/pdf/2012.01894v2); they are not journal page numbers.

Milz–Modi supplies the operational framework. The oscillator calculation, KMS spectral calibration, quantitative contact bounds and cutoff estimates are supplied by the project. An anchor pointer labeled “context” identifies a conceptual connection, not a claim that the anchor proves the project's thermal result. Other research citations retain their attribution role in [Related work][related] without becoming additional educational anchors.

Project pointers refer to the canonical scientific pages in this repository. The [source bridge](milz_modi_bridge.md) connects the selected reading to a complete one-contact experiment and the proof route. Equation labels C, O and the numbered regularization equations belong to their respective pages. The probe is $`S`$, its protected memory is $`R`$, the inverse temperature is $`\beta`$, and the dephasing generator is $`\gamma(Z\rho Z-\rho)`$. There are at most $`N`$ interior contacts. The matching law fixes $`\tau=1/\gamma`$.

## Phase I — Background and preliminaries

### M01 — Qubit coherence as an observable signal

**Central question.** What can change in a qubit without changing its populations?

**Understanding target.** Distinguish diagonal populations from off-diagonal coherence, and distinguish a coherence's magnitude from its phase. Connect both parts to probabilities obtained from a suitable final measurement.

**Dependencies and story role.** No earlier milestone. This is the local observable that both the free calibration and the later witness track.

**Conceptual connection.** A phase difference can carry information even when two experiments have the same amount of decoherence.

**Sources.** Milz–Modi [§IV.A, p.17, and §IV.A.2, p.20][mm17]; [model §1][model]; [witness §1, final two-dimensional states and half trace distance][witness].

### M02 — A dephasing channel and its semigroup calibration

**Central question.** What does an exponential free-decay law specify?

**Understanding target.** Explain the action of the CPTP dephasing channel on every probe input, its composition law, and the convention that the coherence decays as $`e^{-2\gamma t}`$. Keep a family of free channels separate from a claim about interrupted experiments.

**Dependencies and story role.** M01. Moves from one state's signal to a calibrated input-output rule.

**Conceptual connection.** A generator compactly describes unperturbed evolution, while the scope of the observed rule remains an independent question.

**Sources.** Milz–Modi [§IV.B.2, p.22][mm22], [§IV.C, p.26][mm26]; [model §1][model].

### M03 — What is initially in thermal equilibrium?

**Central question.** Which joint state is prepared before the experiment begins?

**Understanding target.** Separate the accessible probe and protected memory from the inaccessible bath. Explain a product preparation with a free-bath thermal state, allowing arbitrary initial correlations between probe and protected memory, and distinguish it from global interacting equilibrium.

**Dependencies and story role.** M01–M02. Supplies the physical preparation on which the reduced channel is based.

**Conceptual connection.** Statements about equilibrium and complete positivity depend on the preparation and the available interventions.

**Sources.** Milz–Modi [§IV.B.4, p.25][mm25], [§V.C, p.37][mm37]; [model §1][model]; [regularization §3][reg].

### M04 — Longitudinal coupling creates conditional bath histories

**Central question.** How can a probe that does not exchange its populations with the bath still become correlated with it?

**Understanding target.** Interpret $`Z\otimes B`$ as two conditional bath evolutions associated with the probe's $`Z`$ eigenvalues. Understand why a coherent probe requires both a forward and a backward history when the bath is traced out.

**Dependencies and story role.** M01 and M03. Identifies the microscopic mechanism behind dephasing before introducing its continuum limit.

**Conceptual connection.** Conditional evolution joins the open-system dilation picture to interference between probe branches.

**Sources.** Milz–Modi [§IV.B.4, p.25][mm25] for dilation context; [operational bound, “Conditional bath histories,” O2–O4][op].

### M05 — Gaussian fluctuations and response are different data

**Central question.** What do the real and imaginary parts of a bath correlation describe?

**Understanding target.** Read $`C(t)=\langle B(t)B(0)\rangle`$ as an ordered two-point correlation. Distinguish the symmetric fluctuation kernel $`R=\mathrm{Re}C`$ from the response kernel $`\eta=-\mathrm{Im}C`$, and identify why a centered Gaussian bath is specified by these second-order data for the present calculation.

**Dependencies and story role.** M03–M04. Gives the two bath ingredients that later separate free decay from controlled memory.

**Conceptual connection.** Loss of interference and the bath's reaction to earlier driving enter the same influence through different terms.

**Sources.** [Calibration, “Thermal covariance and admissible spectral measures,” C1–C2][cal]; [operational bound O2 and O5][op]. This microscopic background is supplied locally.

### M06 — KMS connects temperature to the two spectral parts

**Central question.** How does thermal equilibrium constrain fluctuations and response together?

**Understanding target.** Distinguish the positive-frequency coupling measure $`J_\beta`$ from the symmetrized measure $`\mu=\coth(\beta\omega/2)J_\beta`$. Explain why fixing one of these and imposing finite-temperature KMS constrains the other, without presuming that heating a fixed coupling spectrum preserves a decay law.

**Dependencies and story role.** M05. Adds the physical relation needed for the later inverse-calibration argument.

**Conceptual connection.** Temperature is a constraint on the correlation structure, not merely an adjustable decay coefficient.

**Sources.** [Calibration C1–C2 and “What KMS adds to free calibration”][cal]; [model §1][model]. The thermal relation is a project-supplied bridge.

### M07 — A Gaussian influence combines damping and phase

**Central question.** How do two conditional bath histories alter the probe's coherence?

**Understanding target.** Interpret the history variables $`\delta=a-b`$ and $`\Sigma=a+b`$. Explain how Gaussian averaging produces a real damping term and an ordered response phase, and why Weyl composition contributes a phase that cannot be recovered from damping alone.

**Dependencies and story role.** M04–M06. Combines the local bath ingredients into the calculational object used by the complete process.

**Conceptual connection.** The influence functional records both how paths differ and how earlier common driving affects later differences.

**Sources.** [Operational bound, “Conditional bath histories,” O3–O5][op]; Milz–Modi [§V.D.7, p.47][mm47] for the joint-evolution context.

### M08 — An instrument includes the state change and its record

**Central question.** Why is specifying measurement probabilities alone insufficient for a sequence of experiments?

**Understanding target.** Distinguish an individual outcome map from the complete instrument. Explain how retaining every outcome in a classical register gives a normalized CPTP operation and permits later feedback without conditional renormalization.

**Dependencies and story role.** M01–M02. Introduces the local intervention that changes what a later observation can reveal.

**Conceptual connection.** Backaction makes an operation part of the temporal experiment, while the retained record preserves its unconditional statistics.

**Sources.** Milz–Modi [§V.B, p.35, and §V.B.1, p.36][mm35]; [model §2][model]; [operational bound, “Fixed schedules and recorded testers”][op].

### M09 — A multi-time process answers intervention-dependent questions

**Central question.** What additional object is needed once operations occur between preparation and readout?

**Understanding target.** Describe a process as the rule assigning output statistics to an ordered sequence of operations. Explain why the uncontrolled channel family is only a restricted view of that rule and why intermediate interventions cannot be inferred by inserting free channels without justification.

**Dependencies and story role.** M02 and M08. Lifts local channels and operations into a temporal experiment.

**Conceptual connection.** The distinction between a free channel and a controlled process is the reason the project's question remains open after exact calibration.

**Sources.** Milz–Modi [§V.D, p.40, especially §§V.D.1–V.D.5][mm40]; [model §§1–2][model]; [interpretation, “Fluctuations can be white while response retains memory”][meaning].

### M10 — Markov structure is stronger than channel divisibility

**Central question.** Can perfectly composable free channels coexist with operational memory?

**Understanding target.** Separate CP divisibility from a Markov process whose future is independent of earlier history after the appropriate causal break. Identify that a fixed sequence of independent semigroup segments is a complete comparator, not merely a fit to unperturbed states.

**Dependencies and story role.** M08–M09. Establishes the conceptual distinction the thermal example will quantify.

**Conceptual connection.** Agreement on a restricted collection of temporal observations need not establish agreement on the full process.

**Sources.** Milz–Modi [§VI.A, p.49][mm49], [§VI.A.1, p.51][mm51], [§VI.A.2, p.53][mm53]; [model §2][model].

### M11 — A tester can carry memory between contacts

**Central question.** Which resources belong to the experimenter rather than the bath?

**Understanding target.** Explain how a protected ancilla can be reused, entangled with the probe and read jointly at the end. State the project's admissible class: at most $`N`$ fixed-time interior probe contacts, finite-outcome recorded instruments, feedback in operations, and arbitrary finite protected memory.

**Dependencies and story role.** M03 and M08–M10. Completes the experimental resources over which the theorem optimizes.

**Conceptual connection.** Temporal correlations created deliberately by a tester are distinct from environmental memory that the tester detects.

**Sources.** Milz–Modi [§V.D.6, p.46, Eqs. (189)–(190)][mm46]; [model §2][model]; [operational bound, “Fixed schedules and recorded testers”][op].

### M12 — Operational distance makes all testers comparable

**Central question.** How is the largest possible observable discrepancy defined without favoring one measurement?

**Understanding target.** Interpret half trace distance as a final-event probability difference and $`d_N`$ as its supremum over permitted testers. Explain why complete norm control protects an estimate against enlarging the memory. Keep this comparison with the specified semigroup distinct from optimization over all possible Markov models.

**Dependencies and story role.** M01 and M09–M11. Gives one quantitative objective shared by the universal upper and explicit witness.

**Conceptual connection.** A circuit-level bound controls every final readout and retained record at once.

**Sources.** Milz–Modi [§IV.B.2, p.22][mm22] and [§V.D.6, p.46][mm46] for complete-extension and tester context; [model §2][model]; [operational bound O15–O18][op].

### M13 — Ideal spectra and physical approximation have different limits

**Central question.** How can a well-defined finite-time experiment arise from a singular ideal spectrum?

**Understanding target.** Distinguish admissibility of an integrated coherence exponent from finite equal-time field variance. Separate a continuum spectrum, a mode-frequency cutoff and a finite collection of oscillators; recognize that finite modes do not truncate occupation number or bound the full Hamiltonian spectrum.

**Dependencies and story role.** M03–M07 and M12. Makes the limiting construction and its physical resource boundaries intelligible before the proof uses them.

**Conceptual connection.** Operational convergence of a finite-contact experiment is a different claim from convergence of an unsmeared field operator.

**Sources.** [Calibration C3–C5 and “Zero frequency, deterministic phases and ultraviolet behavior”][cal]; [regularization §§2–3, 8–9][reg].

### M14 — Background synthesis: the calibrated controlled-process problem

**Central question.** What exactly remains to be determined after the free dynamics have been calibrated?

**Understanding target.** Assemble the bath preparation, Gaussian/KMS restriction, all-time free channel, fixed-grid tester class and distance into one problem. Explain why the desired answer needs both a bound for every tester and an experiment that reaches the same order, together with a controlled interpretation of the ideal bath.

**Dependencies and story role.** M01–M13. Integrates the background into the project's precise question.

**Conceptual connection.** Spectral identification fixes the physical process; operational optimization determines how its hidden response can be exposed.

**Sources.** Milz–Modi [§VI.A.1, p.51][mm51], [§VI.A.2, p.53][mm53]; [model §§1–5][model]; [interpretation][meaning].

## Phase II — Narrative and innovation

### M15 — All-time calibration fixes the coupled spectrum

**Central question.** Why is the calibrated spectral family forced within the stated class?

**Understanding target.** Follow the logic from the free exponent $`\Gamma(t)=2\gamma|t|`$ to its distributional second derivative and Fourier uniqueness. Identify the consequences $`\mu=(\gamma/\pi)d\omega`$ and zero static Gaussian variance, while distinguishing uniqueness of coupled correlations from uniqueness of the microscopic bath.

**Dependencies and story role.** M06, M13–M14. Establishes the first load-bearing premise of the particular thermal process.

**Conceptual connection.** Exact temporal calibration is an inverse spectral constraint, rather than a choice of convenient example.

**Sources.** [Calibration, “The free coherence exponent” and “Uniqueness under all-time calibration,” C4–C8][cal]. This identification is supplied by the project.

### M16 — Finite-window calibration leaves genuine freedom

**Central question.** Why does the uniqueness statement require all times?

**Understanding target.** Explain the perturbation that changes the cosine transform outside a chosen observation window while keeping the spectral measure positive and the free channel unchanged inside it. Distinguish this exact nonuniqueness result from a quantitative stability or minimax theorem for approximate calibration.

**Dependencies and story role.** M13 and M15. Fixes the evidential boundary before consequences of exact calibration are drawn.

**Conceptual connection.** A fully specified mathematical calibration class is stronger than a finite experimental record, even when that record is exact.

**Sources.** [Calibration, “Exact calibration on a finite window is not unique,” C11–C13][cal]; [interpretation, “Why calibration scope and preparation matter”][meaning].

### M17 — Thermal detailed balance leaves a response with scale beta

**Central question.** What survives after the symmetric fluctuation spectrum has become white?

**Understanding target.** Connect the identified symmetrized spectrum to $`J_\beta(\omega)=(\gamma/\pi)\tanh(\beta\omega/2)`$ and the positive-time response $`\eta_\beta(t)=(\gamma/\beta)\mathrm{csch}(\pi t/\beta)`$. Explain the finite first moment $`\gamma\beta/4`$ despite the kernel's divergent zero moment.

**Dependencies and story role.** M05–M07 and M15. Extracts the thermal quantity that the contact bound will count.

**Conceptual connection.** White symmetric fluctuations do not remove the response fixed by thermal equilibrium.

**Sources.** [Calibration C9–C10][cal]; [operational bound, “The calibrated response kernel,” O7–O10][op].

### M18 — Contacts expose response between different intervals

**Central question.** Why does the response vanish from each free interval but remain available to controlled experiments?

**Understanding target.** Explain the cancellation $`(a-b)(a+b)=a^2-b^2=0`$ within a constant-history interval and the survival of cross-interval factors. Read the limiting influence as an independent dephasing factor multiplied by a history-dependent phase.

**Dependencies and story role.** M07, M10 and M17. Identifies the local mechanism that makes free-semigroup calibration compatible with controlled memory.

**Conceptual connection.** An intervention changes which earlier common bath driving can influence a later branch difference.

**Sources.** [Operational bound O6, O8 and O11–O12][op]; Milz–Modi [§VI.A.2, p.53][mm53] for the channel/process distinction, with a different microscopic model.

### M19 — The singular bath defines a physical finite-contact process

**Central question.** Why is the limiting influence more than a formal expression?

**Understanding target.** Explain how integrated coefficients of finite physical approximants converge on each finite partition, and why the finite history expansion then preserves complete positivity and causal normalization. Distinguish this existence argument from the quantitative estimate, which must not inherit the number of histories as a prefactor.

**Dependencies and story role.** M04, M07, M11–M13 and M17–M18. Establishes the process on which subsequent operational comparisons act.

**Conceptual connection.** Physical approximants and finite operational questions give meaning to an ideal ultraviolet spectrum.

**Sources.** [Operational bound, “Existence of the finite-intervention cutoff limit,” O19–O21][op]; [regularization §§4–5][reg]; Milz–Modi [§V.D.7, p.47][mm47] for causal-process context.

### M20 — History factors become controlled circuit insertions

**Central question.** How can a scalar influence comparison control every experiment with protected memory?

**Understanding target.** Identify a history monomial with ordered left and right $`Z`$ multiplications in the physical circuit. Explain why each insertion has complete norm one, why it stays on its own interval side of an intervention, and why summing the exponential expansion gives a dimension-independent comparison.

**Dependencies and story role.** M08, M11–M12 and M18–M19. Supplies the bridge from microscopic phase coefficients to a complete operational bound.

**Conceptual connection.** Circuit contractivity avoids bounding every possible history or normalizing individual measurement branches separately.

**Sources.** [Operational bound, “From history factors to circuit insertions,” O13–O18][op]; Milz–Modi [§V.D.6, p.46][mm46] for tester context; [related work §4][related].

### M21 — Each contact is charged one response moment

**Central question.** Why does the maximal discrepancy grow at most linearly with the contact budget when it is small?

**Understanding target.** Explain the boundary-crossing geometry: every cross-interval pair crosses a contact, and a single boundary contributes at most the first response moment. Combine positivity, coefficient counting and the insertion bound to obtain $`d_N\le\min\{1,N\gamma\beta\}`$, uniformly over permitted schedules and finite memory.

**Dependencies and story role.** M17–M20. Assembles the complete upper-bound argument.

**Conceptual connection.** A thermal correlation integral becomes an operational cost per intervention rather than a bath-dimension cost.

**Sources.** [Operational bound, “Charging the response to contacts,” O22–O24 and O1][op]; [model §3][model]; [related work §7, Autonomous-Markovian-Noise][related].

### M22 — A protected reference preserves two useful histories

**Central question.** How can one experiment turn the hidden response into a measurable phase?

**Understanding target.** Describe the reference-controlled alternating branch and the constant branch, their allowed probe contacts, and their final joint readout. Explain why the branches differ for total time $`\tau/2`$, giving coherence multiplier $`e^{-1}`$ at the headline horizon and discrepancy $`e^{-1}|\sin(\Phi_m/2)|`$.

**Dependencies and story role.** M01, M07, M11–M12 and M18. Introduces an explicit admissible tester for the lower bound.

**Conceptual connection.** The reference stores interference while the probe alternates between common bath driving and differential response sensing.

**Sources.** [Witness §1][witness]; Milz–Modi [§V.D.6, p.46][mm46].

### M23 — The witness accumulates response without sign cancellation

**Central question.** Why do more suitable contact pairs strengthen this witness?

**Understanding target.** Identify which ordered interval pairs contribute and why their history factors have the same sign. Explain how retaining only adjacent pairs yields a lower phase bound when interval lengths exceed the thermal scale, while the boundary-moment argument supplies an upper phase bound.

**Dependencies and story role.** M17–M18 and M21–M22. Connects the constructed paths to quantitative phase accumulation.

**Conceptual connection.** The same positive response supports an attainable signal and a universal limitation.

**Sources.** [Witness §2, exact phase and its adjacent-pair and boundary bounds][witness]; [operational bound O10–O11 and O22][op].

### M24 — Schedule selection keeps the lower bound uniform

**Central question.** How is a useful signal maintained when temperature and contact budget vary widely?

**Understanding target.** Explain why the witness uses only an appropriate subset of the available contacts. Relate the small-response choice, the many-contact choice and the single-contact large-memory regime to avoiding phase wrapping and proving one constant lower bound for every finite positive $`\beta`$ and every $`N\ge1`$.

**Dependencies and story role.** M22–M23. Turns a promising phase signal into a uniform operational lower bound.

**Conceptual connection.** A resource allowance is optimized; using all available operations need not be the best strategy.

**Sources.** [Witness §§3–4][witness]; [model §3][model]. The zero-temperature expression is only a comparison limit, not an added endpoint of the theorem.

### M25 — Finite cutoffs have controlled physical Hamiltonians

**Central question.** What makes the finite-cutoff approximants conventional physical bath models?

**Understanding target.** Connect positive oscillator frequencies and $`E_\Omega=\int_0^\Omega J_\beta(\omega)/\omega\,d\omega\lt\infty`$ to semibounded conditional Hamiltonians. Distinguish this form-bound statement from a bounded interaction, a normalizable displaced vacuum, or a trace-class continuum Gibbs density matrix.

**Dependencies and story role.** M03–M06, M13 and M19. Supplies the physical foundation for transferring the ideal-process conclusion to finite bandwidth.

**Conceptual connection.** Semibounded microscopic dynamics can approximate a singular process without imposing a uniform ultraviolet energy or work budget.

**Sources.** [Regularization §§2–3 and 9][reg]; [model §5][model].

### M26 — Cutoff control preserves the operational discrepancy

**Central question.** Can free calibration become arbitrarily accurate while the controlled signal remains nonzero?

**Understanding target.** Connect integrated spectral tails to the tester-uniform error exponent $`16\gamma(N+1)^2/(\pi\Omega)`$. Use the process-distance comparison to interpret persistence of the lower bound, alongside the separate all-time free-exponent error $`8\gamma/(\pi\Omega)`$, at fixed finite contact budget and temperature.

**Dependencies and story role.** M19–M21 and M24–M25. Makes the ideal law robust along the displayed physical cutoff family.

**Conceptual connection.** Improving a free-channel approximation need not erase a response that the approximated process itself retains.

**Sources.** [Regularization §§4–7, especially Eqs. (19), (22)–(30)][reg]; [model §4][model].

### M27 — Finite positive-frequency modes reproduce finite-horizon experiments

**Central question.** Can ordinary finitely many thermal oscillators realize the approximation at a prescribed operational accuracy?

**Understanding target.** Explain how positive-frequency quadrature reproduces the finite-cutoff covariance uniformly on a fixed horizon, and how covariance error becomes a uniform tester error through the insertion estimate. Distinguish finite mode number from finite-dimensional oscillator Hilbert space, and fixed-horizon approximation from approximation uniform over all times.

**Dependencies and story role.** M03, M12–M13, M20 and M25–M26. Completes the constructive physical route behind the cutoff consequence.

**Conceptual connection.** Uniform control of integrated correlations turns a spectral discretization into an approximation of experiments, not merely a plot of a free decay curve.

**Sources.** [Regularization §8, Eqs. (31)–(37)][reg]; [model §§4–5][model].

### M28 — Matching bounds determine the contact resource

**Central question.** What operational scaling follows when the universal upper and explicit witness are combined?

**Understanding target.** Interpret $`c\min\{1,N\gamma\beta\}\le d_N\le\min\{1,N\gamma\beta\}`$ at $`\tau=1/\gamma`$. Explain why any fixed target $`0\lt\delta\le c`$ requires and permits $`N=\Theta(1/(\gamma\beta))`$ in the small-$`\gamma\beta`$ regime, while $`d_0=0`$ and one protected qubit suffices for attainment.

**Dependencies and story role.** M14, M21, M24 and M26–M27. Assembles the principal law with its physical approximation route.

**Conceptual connection.** The thermal time becomes an optimal scale for average contact spacing within the stated one-run experiment.

**Sources.** [Model §§3–5][model]; [interpretation, “A limit on every scheduled tester”][meaning].

### M29 — Locate the contribution and its exact reach

**Central question.** Which conclusion is established beyond known regression failure, and which stronger conclusions remain unsupported?

**Understanding target.** Place the matched contact-temperature law alongside its inherited process framework, Gaussian stability methods and hidden-response mechanism. Distinguish the fixed calibrated process from an approximate-calibration minimax class; separate contact count from repetition cost, work and bandwidth; and distinguish the witness from a certification against every classical-memory explanation.

**Dependencies and story role.** M10–M16 and M25–M28. Connects the complete result to its scientific setting and resource boundaries.

**Conceptual connection.** The strength of a uniform operational theorem comes from precise quantifiers, not from broadening its physical premises.

**Sources.** Milz–Modi [§VI.A.2, p.53][mm53] for the established channel/process distinction; [related work][related]; [model §§2–5][model]; [interpretation][meaning].

### M30 — Narrative synthesis: a calibrated thermal process under control

**Central question.** How do all parts of the argument support one coherent physical conclusion?

**Understanding target.** Connect all-time free calibration to a forced symmetrized spectrum, KMS to the surviving response, contacts to cross-interval phases, circuit insertions to a universal upper, protected histories to attainment, and cutoff control to physical approximants. State the resulting contact law together with the preparation, timing, horizon and calibration assumptions that make it true.

**Dependencies and story role.** M15–M29, grounded in M14. Integrates the narrative into the project's whole scientific account.

**Conceptual connection.** An exact dephasing semigroup can be the free-channel restriction of a controlled thermal process whose memory has a quantitatively resolvable contact scale.

**Sources.** [Model][model]; [interpretation][meaning]; the [calibration][cal], [operational-bound][op], [witness][witness] and [regularization][reg] proofs. Milz–Modi [§V.D.6][mm46] and [§VI.A][mm49] provide the common operational language.

[model]: ../science/model.md
[cal]: ../science/calibration.md
[op]: ../science/operational_bound.md
[witness]: ../science/witness.md
[reg]: ../science/regularization.md
[meaning]: ../science/interpretation.md
[related]: ../references/RELATED_WORK.md
[mm17]: https://arxiv.org/pdf/2012.01894v2#page=17
[mm22]: https://arxiv.org/pdf/2012.01894v2#page=22
[mm25]: https://arxiv.org/pdf/2012.01894v2#page=25
[mm26]: https://arxiv.org/pdf/2012.01894v2#page=26
[mm35]: https://arxiv.org/pdf/2012.01894v2#page=35
[mm37]: https://arxiv.org/pdf/2012.01894v2#page=37
[mm40]: https://arxiv.org/pdf/2012.01894v2#page=40
[mm46]: https://arxiv.org/pdf/2012.01894v2#page=46
[mm47]: https://arxiv.org/pdf/2012.01894v2#page=47
[mm49]: https://arxiv.org/pdf/2012.01894v2#page=49
[mm51]: https://arxiv.org/pdf/2012.01894v2#page=51
[mm53]: https://arxiv.org/pdf/2012.01894v2#page=53
