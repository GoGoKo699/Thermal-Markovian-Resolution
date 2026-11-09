# What exact free calibration determines

For a centered Gaussian thermal bath with positive frequencies and linear longitudinal coupling, matching the free dephasing semigroup at **every time** fixes the coupled spectral measure. At inverse temperature $`\beta\gt0`$, the only admissible measure is

```math
J_\beta(d\omega)
=\frac{\gamma}{\pi}\tanh\!\left(\frac{\beta\omega}{2}\right)d\omega,
\qquad \omega\gt0.
```

Consequently, the [operational control bound](operational_bound.md) applies to every exactly calibrated dilation in this class. The microscopic bath need not be unique, and calibration on a finite time window does not determine this spectrum. Both qualifications are established below.

The [model](model.md) specifies the initial product state, allowed interventions and operational distance. The [regularization account](regularization.md) treats finite frequency cutoffs, for which the free channel approximates the semigroup.

## Thermal covariance and admissible spectral measures

Use units $`\hbar=k_B=1`$. The probe couples through $`Z\otimes B`$, where $`B`$ is a centered linear bosonic field. The bath initially occupies the Gaussian KMS state of its free Hamiltonian, at inverse temperature $`\beta`$, independently of the probe and its protected memory. In a finite-mode realization,

```math
H_B=\sum_\ell\omega_\ell b_\ell^\dagger b_\ell,
\qquad
B=\sum_\ell\left(g_\ell b_\ell+\overline{g_\ell}b_\ell^\dagger\right),
\qquad \omega_\ell\gt0.
```

The coupled spectral measure is $`J=\sum_\ell|g_\ell|^2\delta_{\omega_\ell}`$. Continuous and singular measures are also allowed. For

```math
n_\beta(\omega)=\frac{1}{e^{\beta\omega}-1},
```

the covariance convention is

**Equation (C1).**

```math
\begin{aligned}
C(t)
&=\langle B(t)B(0)\rangle_\beta\\
&=\int_{(0,\infty)}
\left[(n_\beta(\omega)+1)e^{-i\omega t}
+n_\beta(\omega)e^{i\omega t}\right]J(d\omega)\\
&=R(t)-i\eta(t).
\end{aligned}
```

Thus the positive symmetrized measure is

**Equation (C2).**

```math
\mu(d\omega)=\coth\!\left(\frac{\beta\omega}{2}\right)J(d\omega),
\qquad
R(t)=\int_{(0,\infty)}\cos(\omega t)\mu(d\omega),
\qquad
\eta(t)=\int_{(0,\infty)}\sin(\omega t)J(d\omega).
```

These formulas may be interpreted as distributions or through frequency cutoffs. The finite-mode thermal covariance, including its occupation factors, is also given in [Huang–Zhu–Park–Lin, equations (3.21), (3.22) and (3.27)](https://arxiv.org/html/2411.08741v2).

Fix any reference frequency $`\omega_*\gt0`$. We impose the following two finiteness conditions:

**Equation (C3).**

```math
\mu((0,\omega_*])\lt\infty,
\qquad
\int_{(\omega_*,\infty)}\omega^{-2}\mu(d\omega)\lt\infty.
```

Their validity does not depend on the choice of $`\omega_*`$. They say that a finite interval of constant coupling has finite integrated noise variance. Indeed, its frequency filter

```math
f_t(\omega)=\int_0^t e^{i\omega s}ds
```

obeys $`|f_t(\omega)|\le\min\{t,2/\omega\}`$ for $`t\ge0`$, so $`\int |f_t|^2d\mu`$ is finite. Condition (C3) permits an infinite total spectral mass and therefore includes a white symmetrized spectrum. It requires neither a smooth density nor a finite instantaneous variance $`R(0)`$.

Strictly positive-frequency oscillator baths have no zero-frequency oscillator. To make the uniqueness statement explicit about that boundary, one may additionally allow an independent static, centered Gaussian variable of variance $`q\ge0`$. It contributes a constant $`q`$ to $`R(t)`$. The oscillator model itself has $`q=0`$ from the outset.

## The free coherence exponent

For a factorized initial state, the off-diagonal probe element has the form

```math
\rho_{01}(t)=e^{-\Gamma(t)}\rho_{01}(0),
```

after removing any known deterministic probe rotation. Exact Gaussian averaging gives

**Equation (C4).**

```math
\begin{aligned}
\Gamma(t)
&=2qt^2+2\int_{(0,\infty)}|f_t(\omega)|^2\mu(d\omega)\\
&=2qt^2+4\int_{(0,\infty)}
\frac{1-\cos(\omega t)}{\omega^2}\mu(d\omega).
\end{aligned}
```

The factor of four in the second line comes from the difference between the two eigenvalues of $`Z`$. The [influence-functional derivation](operational_bound.md#conditional-bath-histories) establishes this formula without a weak-coupling approximation. In free evolution the response phase vanishes: both conditional forces have the same square, $`(+1)^2=(-1)^2`$. The common scalar bath phase therefore cancels.

The target generator

```math
\mathcal L_\gamma(\rho)=\gamma(Z\rho Z-\rho),
\qquad \gamma\gt0,
```

has coherence factor $`e^{-2\gamma t}`$. Exact all-time calibration means equality of the free channels for every $`t\ge0`$, and hence

**Equation (C5).**

```math
\Gamma(t)=2\gamma t\quad(t\ge0).
```

## Uniqueness under all-time calibration

**Proposition.** Let $`\mu`$ be a positive Borel measure on $`(0,\infty)`$ satisfying (C3), and let $`q\ge0`$ be finite. If (C4) satisfies (C5), then

**Equation (C6).**

```math
q=0,
\qquad
\mu(d\omega)=\frac{\gamma}{\pi}d\omega,
\qquad
J(d\omega)=\frac{\gamma}{\pi}
\tanh\!\left(\frac{\beta\omega}{2}\right)d\omega.
```

These are equalities of measures. In particular, all atomic and singular-continuous components of the coupled positive-frequency spectrum vanish. If a spectral density was assumed initially, its value is fixed almost everywhere.

### Proof

The inequality $`1-\cos x\le\min\{2,x^2/2\}`$ and (C3) imply that $`\Gamma`$ is finite, continuous and at most quadratic in time. Extend it evenly to the real line. The even spectral measure

**Equation (C7).**

```math
M=q\delta_0+\frac12\mu+\frac12\mu^{\mathrm{ref}}
```

is tempered, where $`\mu`$ is embedded on the positive half-line and $`\mu^{\mathrm{ref}}`$ is its reflection onto the negative half-line.

Differentiating (C4) twice in the sense of tempered distributions gives

**Equation (C8).**

```math
\Gamma''(t)=4R(t),
\qquad
R(t)=q+\int_{(0,\infty)}\cos(\omega t)\mu(d\omega)
=\int_{\mathbb R}e^{i\omega t}M(d\omega).
```

The interchange can be checked against a Schwartz test function. Before integrating by parts, the high-frequency contribution is bounded by a constant times $`\omega^{-2}`$. At low frequency, $`(1-\cos(\omega t))/\omega^2`$ is bounded by $`t^2/2`$. Both are integrable under (C3). After integration by parts, the test function's Fourier transform decays rapidly, which justifies the last integral in (C8).

By (C5) and evenness, $`\Gamma(t)=2\gamma|t|`$. Therefore

```math
\Gamma''=4\gamma\delta_0,
\qquad R=\gamma\delta_0.
```

With the Fourier convention in (C8), the transform of $`(\gamma/2\pi)d\omega`$ is $`\gamma\delta_0`$. Uniqueness of the Fourier transform of tempered distributions yields

```math
M(d\omega)=\frac{\gamma}{2\pi}d\omega.
```

Its zero-frequency atom is zero, so $`q=0`$. Restriction to positive frequencies gives $`\mu=(\gamma/\pi)d\omega`$. Finally, (C2) implies

```math
J(d\omega)=\tanh\!\left(\frac{\beta\omega}{2}\right)\mu(d\omega),
```

which proves (C6).

An equivalent proof uses the uniqueness of the symmetric Lévy–Khintchine representation. Equation (C4) has Gaussian variance coefficient $`4q`$ and a symmetric Lévy measure whose positive half is $`2\omega^{-2}\mu(d\omega)`$. The exponent $`2\gamma|t|`$ has zero Gaussian component and Cauchy Lévy density $`2\gamma/(\pi\omega^2)`$ on the whole real line. Standard triplet uniqueness gives the same result; see [Pitman, Lecture 26, Theorem 1.6](https://www.stat.berkeley.edu/users/pitman/s205s03/levy.pdf).

## What KMS adds to free calibration

Free coherence determines the symmetrized spectrum. Thermal detailed balance then determines the response. To see this directly, let $`S_+`$ and $`S_-`$ denote the positive- and reflected negative-frequency measures in (C1). KMS gives

**Equation (C9).**

```math
S_-(d\omega)=e^{-\beta\omega}S_+(d\omega),
\qquad
\mu=S_++S_-,
\qquad
J=S_+-S_-.
```

Solving these measure identities yields $`J=\tanh(\beta\omega/2)\mu`$. For the uniquely calibrated spectrum, the response is

**Equation (C10).**

```math
\eta_\beta(t)=\frac{\gamma}{\beta}
\mathrm{csch}\!\left(\frac{\pi t}{\beta}\right),
\qquad t\gt0,
```

with the transform understood through ultraviolet regularization. Its derivation and first moment appear in the [operational-bound proof](operational_bound.md#the-calibrated-response-kernel).

Gaussianity and linear coupling make the two-point function determine every finite-history influence. Thus, at fixed $`\beta`$ and $`\gamma`$, all exactly calibrated baths in this class give the same controlled process at finite intervention schedules. This is the sense in which the contact-temperature law is universal here.

The result does not identify a microscopic bath Hamiltonian or mode decomposition. Uncoupled modes, multiplicities and equivalent realizations are invisible to the probe. Nor does free calibration determine the temperature: different choices of $`\beta`$ have different response spectra while producing the same free semigroup. Non-Gaussian baths, nonthermal stationary states and other coupling forms are outside this uniqueness statement.

## Zero frequency, deterministic phases and ultraviolet behavior

A zero-frequency harmonic oscillator has no ordinary normalized Gibbs state. If a static commuting Gaussian component is nevertheless added to the model, its contribution is the term $`2qt^2`$ in (C4), and all-time calibration forces it to vanish. The removable limit

```math
\lim_{\omega\to0}\frac{1-\cos(\omega t)}{\omega^2}
=\frac{t^2}{2}
```

explains why a zero-frequency covariance atom cannot be ignored.

A nonzero deterministic bath mean has a different effect: it induces a coherent $`Z`$ rotation. Centering excludes that mean. A bare probe Hamiltonian $`(\Omega/2)Z`$ contributes the factor $`e^{-i\Omega t}`$ to the coherence. Matching the specified target without a Hamiltonian term fixes the net rotation to zero. If calibration is defined up to a known deterministic rotation, the spectral conclusion is unchanged. A common identity energy shift has no observable effect.

The forced symmetrized measure has infinite total mass. Exact nontrivial semigroup calibration therefore lies outside the class with finite instantaneous bath-field variance. For comparison, if $`\mu((0,\infty))\lt\infty`$, dominated convergence in (C4) gives a quadratic short-time exponent, which cannot equal $`2\gamma t`$ near zero. The calibrated process is consequently defined through its finite-intervention cutoff limit. A finite cutoff gives an approximation, quantified in [regularization.md](regularization.md).

## Exact calibration on a finite window is not unique

The all-time hypothesis is essential under (C3). The following construction gives positive thermal spectra that agree with the target free channel on a prescribed window but differ outside it.

Fix a window length $`T_0\gt0`$. Choose a nonzero, real, even, smooth compactly supported function $`K`$ with support outside $`[-T_0,T_0]`$. Define its inverse cosine transform by

**Equation (C11).**

```math
h(\omega)=\frac2\pi\int_0^\infty K(t)\cos(\omega t)dt.
```

Then $`h`$ is a bounded real Schwartz function and

```math
\int_0^\infty h(\omega)\cos(\omega t)d\omega=K(t).
```

Choose a nonzero real $`\lambda`$ satisfying

```math
|\lambda|\,\|h\|_\infty\lt\frac{\gamma}{2\pi}.
```

The measure

**Equation (C12).**

```math
\mu_\lambda(d\omega)
=\left[\frac\gamma\pi+\lambda h(\omega)\right]d\omega
```

is strictly positive and satisfies (C3). Its dephasing exponent differs from the white-spectrum exponent by a smooth even function obeying

**Equation (C13).**

```math
\begin{aligned}
(\Gamma_\lambda-\Gamma_0)''&=4\lambda K,\\
(\Gamma_\lambda-\Gamma_0)(0)&=0,\\
(\Gamma_\lambda-\Gamma_0)'(0)&=0.
\end{aligned}
```

Because $`K`$ vanishes on the calibration window, (C13) implies

```math
\Gamma_\lambda(t)=2\gamma|t|
\qquad\text{for }|t|\le T_0.
```

Nevertheless, $`\mu_\lambda\ne\mu_0`$. At the same temperature, define

```math
J_\lambda(d\omega)
=\tanh\!\left(\frac{\beta\omega}{2}\right)\mu_\lambda(d\omega).
```

This is another positive KMS-compatible coupled spectrum. It gives exact free calibration on $`[0,T_0]`$ without the all-time spectral identity. Thus finite-window calibration alone does not establish the universal controlled process above. Approximate calibration requires separate assumptions and is not covered by this proposition.

## Attribution and further reading

The thermal covariance formula, Gaussian influence method and Fourier/Lévy uniqueness ingredients are established tools. Their use here makes the scope of the control-resolution statement explicit. The [related-work account](../references/RELATED_WORK.md) distinguishes this spectral classification from earlier examples in which semigroup free evolution coexists with intervention-dependent phases.
