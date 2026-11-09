# The operational bound under fixed interventions

A thermal response can be invisible in every free dephasing channel and still affect controlled experiments. For the exactly calibrated Gaussian thermal process, the effect of at most $`N`$ preassigned interventions obeys

**Equation (O1).**

```math
d_N(\beta,\gamma,\tau)
\le
\min\left\{1,\frac{e^{N\gamma\beta}-1}{2}\right\}
\le\min\{1,N\gamma\beta\}.
```

The proof is uniform over the intervention times and over protected memories of arbitrary finite dimension. Instruments may be noncommuting, may retain classical outcomes, and may choose later operations using those records. The horizon $`\tau`$ is arbitrary in this upper bound; the matching contact-temperature law uses $`\gamma\tau=1`$.

The [model](model.md) defines the operational distance. The [calibration theorem](calibration.md) shows why the spectrum below is forced within the stated all-time Gaussian KMS class. The [witness](witness.md) supplies the matching lower order, and [regularization](regularization.md) quantifies finite frequency cutoffs.

## Fixed schedules and recorded testers

Fix a schedule

```math
0=t_0\lt t_1\lt\cdots\lt t_N\lt t_{N+1}=\tau,
\qquad L=N+1,
\qquad I_j=(t_{j-1},t_j).
```

A tester begins with a state of the probe and a finite protected memory. Between intervals it applies a finite-outcome quantum instrument. Store each outcome in a classical register and include the subsequent feedback operation in the next map. The resulting maps $`\mathcal A_1,\ldots,\mathcal A_{L-1}`$ on the probe, memory and records are CPTP. Their dimensions may grow with the record, but are finite for each tester. Initial preparation and final readout are free.

Between contacts, the probe has only the specified longitudinal interaction with the bath. There is no continuous noncommuting probe drive. Memory-only evolution can be absorbed into the neighboring tester map. Times are fixed before the experiment; outcome-dependent operations are allowed, while outcome-dependent choices of times are outside this class.

For any fixed tester, the maximal difference of a final-event probability is half the trace distance of its two normalized output states. The distance $`d_N`$ takes the supremum over the allowed testers and schedules with at most $`N`$ contacts. Keeping all outcomes in the output state is essential: the probability of a rare herald is counted, without dividing by it.

## Conditional bath histories

First take a finite collection of harmonic modes in a normalized free-bath thermal state, independently of the probe and memory. In the interaction picture of the free bath,

```math
B(t)=\sum_\ell\left(
g_\ell b_\ell e^{-i\omega_\ell t}
+\overline g_\ell b_\ell^\dagger e^{i\omega_\ell t}
\right).
```

Write $`C(t)=\langle B(t)B(0)\rangle_\beta=R(t)-i\eta(t)`$. The commutator is a scalar:

**Equation (O2).**

```math
[B(t),B(s)]=-2i\eta(t-s)I.
```

Let $`a(t)\in\{+1,-1\}`$ be a piecewise-constant probe history. Its conditional bath evolution is

```math
U_a=\mathcal T\exp\left[-i\int_0^\tau a(t)B(t)dt\right]
=e^{i\varphi[a]}D(\xi[a]),
```

where $`D`$ is the multimode displacement and

**Equation (O3).**

```math
\varphi[a]=\int_{0\lt s\lt t\lt\tau}
a(t)a(s)\eta(t-s)\,ds\,dt.
```

This is exact: the Magnus expansion terminates after its scalar commutator term. The displacement amplitude in mode $`\ell`$ is

```math
\xi_\ell[a]=-i\overline g_\ell\int_0^\tau a(t)e^{i\omega_\ell t}dt.
```

For two histories $`a,b`$, define

```math
\delta(t)=a(t)-b(t),
\qquad
\Sigma(t)=a(t)+b(t).
```

The bath influence is $`F(a,b)=\mathrm{Tr}_B(U_a\rho_\beta U_b^\dagger)`$. Weyl composition gives

**Equation (O4).**

```math
\varphi[a]-\varphi[b]
+\mathrm{Im}\langle\xi[b],\xi[a]\rangle
=\int_{0\lt s\lt t\lt\tau}
\delta(t)\Sigma(s)\eta(t-s)\,ds\,dt.
```

Gaussian averaging of the remaining displacement then yields

**Equation (O5).**

```math
\begin{aligned}
F(a,b)=\exp\Bigg[&-\frac12\int_0^\tau\!\int_0^\tau
\delta(t)\delta(s)R(t-s)\,ds\,dt\\
&+i\int_{0\lt s\lt t\lt\tau}
\delta(t)\Sigma(s)\eta(t-s)\,ds\,dt\Bigg].
\end{aligned}
```

Changing the convention for the off-diagonal element reverses the response phase but leaves the bounds unchanged. Equation (O5) uses neither weak coupling nor a Markov approximation.

On one interval, both histories are constant and

**Equation (O6).**

```math
\delta_j\Sigma_j=(a_j-b_j)(a_j+b_j)=a_j^2-b_j^2=0.
```

Thus the response contributes only between distinct intervals. This cancellation will make the singular short-time kernel manageable.

## The calibrated response kernel

The [all-time calibration theorem](calibration.md#uniqueness-under-all-time-calibration) fixes

**Equation (O7).**

```math
J_\beta(d\omega)
=\frac\gamma\pi\tanh\!\left(\frac{\beta\omega}{2}\right)d\omega,
\qquad
\mu(d\omega)=\frac\gamma\pi d\omega.
```

In the cutoff limit, the real covariance is $`R(t)=\gamma\delta_0(t)`$. The real part of (O5) is therefore exactly the independent Markov dephasing factor

**Equation (O8).**

```math
F_0(a,b)=\prod_{j=1}^L
\exp\left[-\frac\gamma2|I_j|(a_j-b_j)^2\right].
```

For $`t\gt0`$, the regulated sine transform of (O7) is

**Equation (O9).**

```math
\eta_\beta(t)=\frac\gamma\beta
\mathrm{csch}\!\left(\frac{\pi t}{\beta}\right).
```

One way to obtain (O9) is to differentiate $`\tanh(\beta\omega/2)`$ in frequency, use the Fourier transform of $`\mathrm{sech}^2`$, and integrate back in the distributional sense. Equivalently, an Abel regulator gives

```math
\lim_{\varepsilon\downarrow0}
\int_0^\infty e^{-\varepsilon\omega}
\tanh\!\left(\frac{\beta\omega}{2}\right)
\sin(\omega t)d\omega
=\frac\pi\beta\mathrm{csch}\!\left(\frac{\pi t}{\beta}\right).
```

The kernel is positive on positive times. It behaves as $`\gamma/(\pi t)`$ near zero, so its zero moment diverges. Its first moment is finite:

**Equation (O10).**

```math
\begin{aligned}
\int_0^\infty t\eta_\beta(t)dt
&=\frac{\gamma\beta}{\pi^2}
\int_0^\infty\frac{u}{\sinh u}du\\
&=\frac{\gamma\beta}{4}.
\end{aligned}
```

For the last identity, expand $`1/\sinh u=2\sum_{r\ge0}e^{-(2r+1)u}`$, integrate term by term, and use the sum of the inverse odd squares.

For $`j\gt k`$, let

**Equation (O11).**

```math
\eta_{jk}=\int_{I_j}dt\int_{I_k}ds\,\eta_\beta(t-s).
```

These integrals are finite, including adjacent intervals. Near their shared boundary the rectangle supplies an overlap factor bounded by the separation $`t-s`$, which cancels the kernel's $`1/(t-s)`$ singularity. Equations (O5), (O6) and (O8) give

**Equation (O12).**

```math
F_\beta(a,b)
=F_0(a,b)
\exp\left[i\sum_{j\gt k}\eta_{jk}(a_j-b_j)(a_k+b_k)\right].
```

An entrywise bound on this phase is insufficient by itself for an operational distance bound. The next step identifies every term with a norm-controlled circuit.

## From history factors to circuit insertions

Let $`P_+`$ and $`P_-`$ be the probe's $`Z`$ eigenprojectors, extended by the identity on the protected memory and records. For $`a,b\in\{+1,-1\}^L`$, define a linear history map recursively by

**Equation (O13).**

```math
\begin{aligned}
X_1&=P_{a_1}XP_{b_1},\\
X_j&=P_{a_j}\mathcal A_{j-1}(X_{j-1})P_{b_j},
\qquad j=2,\ldots,L,\\
\mathcal H_{a,b}(X)&=X_L.
\end{aligned}
```

For an influence kernel $`F`$, the tester output map is

**Equation (O14).**

```math
\mathcal T_F(X)=\sum_{a,b}F(a,b)\mathcal H_{a,b}(X).
```

Each $`\mathcal H_{a,b}`$ has diamond norm at most one, since it is a composition of CPTP maps and left/right multiplications by orthogonal projectors. The stronger bound needed below applies after summing the histories with their physical influence.

### Insertion lemma

Let $`F`$ arise from a physical longitudinal probe-bath evolution, or from a finite-history limit of such evolutions. For nonnegative integer vectors $`p,q`$, define the history monomial

```math
m_{p,q}(a,b)=\prod_{j=1}^L a_j^{p_j}b_j^{q_j}.
```

Then, for every fixed tester,

**Equation (O15).**

```math
\|\mathcal T_{F m_{p,q}}\|_\diamond\le1.
```

**Proof for a physical dilation.** Keep the bath in the circuit. At the end of interval $`j`$, before the next tester map, insert

**Equation (O16).**

```math
X\longmapsto
(Z^{p_j}\otimes I)X(Z^{q_j}\otimes I).
```

In the history expansion this multiplies the coefficient by exactly $`a_j^{p_j}b_j^{q_j}`$. The insertion commutes with the longitudinal evolution within that interval. No insertion is moved across a tester operation, so arbitrary noncommuting instruments present no obstruction.

Left and right multiplication by unitaries have completely bounded trace norm one, even when their product is not a positive map. Initial attachment of the normalized bath state, joint unitary evolution, the recorded tester maps and final bath partial trace also have diamond norm one. Their composition proves (O15). Tensoring an arbitrary untouched reference leaves every step valid; therefore the bound is independent of the protected-memory dimension.

For $`F_0`$, summing each interval in (O14) produces its CPTP dephasing channel. Equation (O16) inserts left/right $`Z`$ multiplication next to that channel, giving the same proof directly for the Markov process.

The extension to a limiting influence follows from the finite-history norm convergence established below. The inserted maps are linear maps, not necessarily quantum channels; their norm bound is what is used.

### Exponent comparison

Suppose two kernels satisfy

**Equation (O17).**

```math
F'(a,b)=F(a,b)e^{G(a,b)},
\qquad
G(a,b)=\sum_\mu c_\mu m_\mu(a,b),
\qquad
S=\sum_\mu|c_\mu|,
```

where the $`m_\mu`$ are history monomials and the base kernel $`F`$ satisfies (O15). A product of such monomials is another monomial. Expand the scalar exponential, apply (O15) to every term, and sum the absolute coefficients:

**Equation (O18).**

```math
\begin{aligned}
\|\mathcal T_{F'}-\mathcal T_F\|_\diamond
&\le\sum_{r=1}^\infty\frac{S^r}{r!}\\
&=e^S-1.
\end{aligned}
```

The series is absolutely convergent in diamond norm. Equation (O18) has no factor for the number of histories, memory dimension or outcome branches. If both output maps describe physical processes, their output states are normalized, and any final-event discrepancy is bounded by half the right-hand side.

This argument is a discrete longitudinal version of established Gaussian covariance-perturbation methods. In particular, [Huang–Zhu–Park–Lin, Theorem 2.9 and equation (2.46)](https://arxiv.org/html/2411.08741v2) identify inserted reduced superoperators with a contractive full-system circuit. [Liu–Lu, Theorem 1](https://arxiv.org/html/2408.04009v3) gives a related bound through diagrammatic expansions. Here the explicit history representation also accommodates recorded instruments at fixed contacts.

## Existence of the finite-intervention cutoff limit

The infinite-cutoff process is defined by limits of physical Gaussian models. This construction is separate from the coefficient estimate in (O18).

For a cutoff $`\Omega`$, use $`J_\beta(d\omega)\mathbf1_{\omega\le\Omega}`$. Let

```math
f_j(\omega)=\int_{I_j}e^{i\omega t}dt.
```

The integrated real coefficients are

**Equation (O19).**

```math
R^\Omega_{jk}
=\frac\gamma\pi\int_0^\Omega
\mathrm{Re}\!\left[f_j(\omega)\overline{f_k(\omega)}\right]d\omega,
```

and the cross-interval response coefficients use the imaginary part with weight $`J_\beta`$. At low frequency these integrands are bounded. At high frequency,

```math
|f_j(\omega)f_k(\omega)|\le\frac4{\omega^2},
```

so every coefficient has an absolutely convergent tail. Their limits are

**Equation (O20).**

```math
R_{jk}=\gamma|I_j|\,\delta_{jk},
\qquad
\eta_{jk}=\int_{I_j}dt\int_{I_k}ds\,\eta_\beta(t-s)
\quad(j\gt k).
```

For finite cutoff, finite-mode spectral discretizations approximate these finitely many coefficients with positive weights and normalized oscillator Gibbs states. The low-frequency integrals are regular after the coupling and thermal factors are combined. One may therefore take finite-mode approximations first, and then increase the frequency cutoff. No infinite-volume thermal density matrix is required for this construction.

Every history influence converges to (O12). For any fixed $`L`$, equations (O13)–(O14) imply

**Equation (O21).**

```math
\|\mathcal T_{F_\Omega m}-\mathcal T_{F_\beta m}\|_\diamond
\le\sum_{a,b}|F_\Omega(a,b)-F_\beta(a,b)|,
```

for every history monomial $`m`$. This convergence is uniform over protected-memory dimensions and testers at the fixed schedule. The right-hand side contains finitely many terms. It may be bounded crudely by $`4^L`$ times the largest coefficient error, but it is used only to establish the limit and to pass the norm bound (O15) to that limit. It does not enter the operational rate (O18).

The uninserted limiting maps remain CPTP. The finite-time causal consistency conditions also pass to the limit, because they hold for every approximating physical process. This defines the limiting process on each finite schedule. In particular, an exactly white symmetrized spectrum does not require a claim that the unregularized interaction is a bounded Hamiltonian.

The [regularization theorem](regularization.md) uses (O18), rather than the crude history count in (O21), to obtain a quantitative cutoff error uniform over the same tester class.

## Charging the response to contacts

Apply (O18) to (O12), using the Markov influence $`F_0`$ as the base. Each factor

```math
(a_j-b_j)(a_k+b_k)
=a_ja_k+a_jb_k-b_ja_k-b_jb_k
```

has four monomials. Since $`\eta_{jk}\ge0`$, its total coefficient budget is bounded by

**Equation (O22).**

```math
S\le4\sum_{j\gt k}\eta_{jk}.
```

For any pair $`s\lt t`$ lying in distinct intervals, at least one contact lies between them. Charge the pair to every such contact, which can only increase the integral because the kernel is positive. For a contact at $`c`$,

**Equation (O23).**

```math
\begin{aligned}
\int_0^c ds\int_c^\tau dt\,\eta_\beta(t-s)
&=\int_0^c dx\int_0^{\tau-c}dy\,\eta_\beta(x+y)\\
&\le\int_0^\infty u\eta_\beta(u)du\\
&=\frac{\gamma\beta}{4}.
\end{aligned}
```

There are at most $`N`$ contacts. Consequently,

**Equation (O24).**

```math
\sum_{j\gt k}\eta_{jk}\le\frac{N\gamma\beta}{4},
\qquad S\le N\gamma\beta.
```

Combining (O18) with the final-event trace-distance bound proves the first inequality in (O1). To obtain its second inequality, set $`x=N\gamma\beta`$. For $`0\le x\le1`$, convexity gives

```math
e^x-1\le(e-1)x\le2x.
```

For $`x\ge1`$, use the trivial probability-distance bound one. With no contacts, $`N=0`$, the discrepancy is exactly zero, as required by free calibration.

The mechanism is the finite first moment (O10). A direct bound on the zero moment of the response would diverge. The exact same-interval cancellation and the contact geometry provide the additional factor of time that makes the operational estimate finite.

## Scope of the conclusion

At the normalized horizon $`\tau=1/\gamma`$, the [coherent witness](witness.md) gives the complementary lower order, so the operational distance has scale $`\min\{1,N\gamma\beta\}`$. The upper allows arbitrary finite protected memory and arbitrary recorded feedback operations at the chosen contacts.

Adaptive timing is a different class: the union of the branches of a timing tree can have many more contact locations than the number encountered on one realization. Continuous noncommuting driving between contacts also requires another argument. Neither is inferred from this proof. Likewise, [spectral uniqueness](calibration.md) concerns exact calibration at all times; it does not turn approximate or finite-window calibration into a universal controlled-error floor.

The distinction between free semigroup evolution and intervention-dependent phases is established in [Lonigro–Chruściński, Proposition 3.2 and equation (67)](https://arxiv.org/pdf/2202.11056). The [related-work account](../references/RELATED_WORK.md) places the thermal contact law and its bounds alongside that result and the covariance-perturbation literature.
