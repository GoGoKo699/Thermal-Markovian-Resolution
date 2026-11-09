# A protected-reference witness

The calibrated thermal process can differ from its Markov comparison by a constant amount when the number of available contacts is of order the inverse thermal memory parameter. This page gives an explicit protocol and a lower bound valid at every finite temperature.

The setting is the [calibrated longitudinal model](model.md). The horizon is $`\tau=1/\gamma`$, the inverse temperature satisfies $`0\lt\beta\lt\infty`$, and

```math
r=\gamma\beta.
```

There are at most $`N`$ preassigned **internal** contact times. Preparation at time zero and the final joint measurement are free. Contact operations may act on the probe and a protected reference. The parameters of the two processes being compared are known; the schedule and final measurement may depend on those parameters. The lower bound optimizes over allowed fixed schedules. It does not assert that every schedule attains the bound.

For the operational distance defined in the model, the result is

```math
d_N\ge c\min\{1,N\gamma\beta\},
\qquad
c=\frac{e^{-1}}{4\pi\sinh\pi}
\approx 0.0025349014,
\qquad N\ge1.
```

The constant is conservative. The proof establishes the order uniformly in temperature; it does not optimize the numerical coefficient.

## 1. Two coherent histories

Prepare the protected reference $`R`$ in $`|+\rangle_R=(|0\rangle_R+|1\rangle_R)/\sqrt2`$ and the probe $`S`$ in its $`Z=+1`$ eigenstate. Choose an integer $`m\ge1`$ and divide the horizon into $`2m`$ equal intervals of length

```math
h=\frac{\tau}{2m}.
```

At every internal boundary $`h,2h,\ldots,(2m-1)h`$, apply $`X`$ to the probe conditional on $`R=1`$. The two reference branches then follow the histories

```math
a_j=+1,
\qquad
b_j=(-1)^{j-1},
\qquad j=1,\ldots,2m.
```

This protocol uses exactly $`2m-1`$ internal contacts. The reference does not couple to the bath between contacts.

Define the forward/backward difference and sum by $`\delta=a-b`$ and $`\Sigma=a+b`$. On odd intervals the branches agree, so $`\delta=0`$ and $`\Sigma=2`$. On even intervals they differ, so $`\delta=2`$ and $`\Sigma=0`$. In particular,

```math
\delta(t)\Sigma(s)\in\{0,4\}.
```

Every nonzero response term has the same sign. The protocol therefore avoids cancellation between the phases accumulated at different contacts.

The exact influence functional is

```math
F[a,b]
=\exp\left[
-\frac{\gamma}{2}\int_0^\tau\delta(t)^2\,dt
+i\int_{0\lt s\lt t\lt\tau}
\delta(t)\Sigma(s)\eta_\beta(t-s)\,ds\,dt
\right],
```

where

```math
\eta_\beta(u)=\frac{\gamma}{\beta}
\mathrm{csch}\left(\frac{\pi u}{\beta}\right),
\qquad u\gt0.
```

The branches differ for exactly half the horizon. Consequently their coherence has modulus

```math
\exp\left[-\frac{\gamma}{2}\cdot4\cdot\frac{\tau}{2}\right]
=e^{-1}
```

in both the thermal and Markov processes. The Markov coherence is real. Write the thermal coherence as $`e^{-1+i\Phi_m}`$.

At the final time, the two branch states are the orthogonal joint states $`|0\rangle_R|+z\rangle_S`$ and $`|1\rangle_R|-z\rangle_S`$. In this two-dimensional subspace the two output density matrices are

```math
\rho_\beta^{(m)}
=\frac12
\begin{pmatrix}
1&e^{-1+i\Phi_m}\\
e^{-1-i\Phi_m}&1
\end{pmatrix},
\qquad
\rho_{\mathrm M}^{(m)}
=\frac12
\begin{pmatrix}
1&e^{-1}\\
e^{-1}&1
\end{pmatrix}.
```

An optimal final joint measurement distinguishes them with final-event discrepancy

```math
d_m^{\mathrm{wit}}
=\frac12\|\rho_\beta^{(m)}-\rho_{\mathrm M}^{(m)}\|_1
=e^{-1}\left|\sin\left(\frac{\Phi_m}{2}\right)\right|.
```

No extra internal contact is needed to recombine the branches. Their joint coherence is already accessible to the allowed final measurement.

## 2. Exact phase and elementary bounds

For two intervals separated by $`d`$ interval lengths, define

```math
I_d(h)
=\int_{(d-1)h}^{(d+1)h}
\bigl(h-|u-dh|\bigr)\eta_\beta(u)\,du.
```

An earlier agreeing interval and a later differing interval have odd separation $`d=2q+1`$. There are $`m-q`$ such pairs. Therefore

```math
\Phi_m
=4\sum_{q=0}^{m-1}(m-q)I_{2q+1}(h).
```

The integrals are finite despite the short-time behavior $`\eta_\beta(u)\sim\gamma/(\pi u)`$: for adjacent intervals the triangular weight vanishes linearly at the origin. Positivity of the kernel makes every summand nonnegative.

### Adjacent pairs give the lower phase bound

If $`h\ge\beta`$, retain only adjacent agreeing/differing pairs:

```math
\Phi_m
\ge4m\int_0^h\int_0^h\eta_\beta(x+y)\,dx\,dy
\ge4m\int_0^\beta u\eta_\beta(u)\,du.
```

After setting $`v=u/\beta`$, use $`\sinh(\pi v)\le\sinh\pi`$ for $`0\le v\le1`$ to obtain

```math
\int_0^\beta u\eta_\beta(u)\,du
=\gamma\beta\int_0^1\frac{v}{\sinh(\pi v)}\,dv
\ge\frac{\gamma\beta}{2\sinh\pi}.
```

Thus

```math
\boxed{\displaystyle
\Phi_m\ge\frac{2m\gamma\beta}{\sinh\pi}
\quad\text{if }h\ge\beta.}
```

### Charging crossed boundaries gives the upper phase bound

Every contributing pair $`s\lt t`$ crosses at least one internal boundary. Charging the pair to every boundary it crosses only increases the positive integral. A single boundary contributes at most

```math
\int_0^\infty u\eta_\beta(u)\,du
=\frac{\gamma\beta}{\pi^2}
\int_0^\infty\frac{v}{\sinh v}\,dv
=\frac{\gamma\beta}{4}.
```

The last identity follows by expanding $`1/\sinh v=2\sum_{k=0}^\infty e^{-(2k+1)v}`$ and integrating the positive series. Since there are $`2m-1`$ boundaries and the history factor is four,

```math
\boxed{\displaystyle
\Phi_m\le(2m-1)\gamma\beta.}
```

This estimate is useful for selecting a witness whose phase does not wrap.

## 3. A single contact controls the low-temperature regime

For fixed $`u\gt0`$, the response kernel increases with $`\beta`$. Indeed, writing $`x=\pi u/\beta`$ gives

```math
\eta_\beta(u)
=\frac{\gamma}{\pi u}\frac{x}{\sinh x},
```

and $`x/\sinh x`$ decreases for positive $`x`$. Moreover, $`\eta_\beta(u)\le\gamma/(\pi u)`$.

For $`m=1`$, monotone convergence yields

```math
\Phi_1\uparrow
\frac{4\gamma}{\pi}
\int_0^{\tau/2}\int_0^{\tau/2}\frac{dx\,dy}{x+y}
=\frac{4\log2}{\pi}
\lt\pi
\qquad\text{as }\beta/\tau\to\infty.
```

Thus $`d_1^{\mathrm{wit}}=e^{-1}\sin(\Phi_1/2)`$ increases with inverse temperature $`\beta`$ and never encounters phase wrapping. The zero-temperature expression is used only as a limit and a comparison bound; the theorem concerns finite $`\beta`$.

## 4. Uniform lower bound for every contact budget

Let

```math
M=\left\lfloor\frac{N+1}{2}\right\rfloor,
\qquad
c=\frac{e^{-1}}{4\pi\sinh\pi}.
```

Any $`1\le m\le M`$ is an allowed witness. The following cases cover all $`r=\gamma\beta\gt0`$.

### Small accumulated response

Suppose $`r\le1/4`$ and $`Mr\le1/4`$. Choose $`m=M`$. Then $`h\ge2\beta`$ and $`\Phi_m\le2mr\le1/2`$. Using $`\sin(\Phi_m/2)\ge\Phi_m/\pi`$ gives

```math
d_m^{\mathrm{wit}}
\ge\frac{2e^{-1}mr}{\pi\sinh\pi}
=8cmr
\ge4cNr
\ge c\min\{1,Nr\}.
```

The inequality $`2M\ge N`$ accounts for even and odd contact budgets.

### Many contacts at small thermal memory

Suppose $`r\le1/4`$ and $`Mr\gt1/4`$. Choose

```math
m=\left\lfloor\frac{1}{4r}\right\rfloor.
```

This satisfies $`1\le m\le M`$. Since $`\lfloor a\rfloor\ge a/2`$ for $`a\ge1`$,

```math
\frac18\le mr\le\frac14.
```

The same phase bounds apply and give

```math
d_m^{\mathrm{wit}}
\ge8cmr
\ge c
\ge c\min\{1,Nr\}.
```

The protocol intentionally leaves some contacts unused. Additional contacts are not needed after a constant discrepancy has been reached.

### Large thermal memory

Suppose $`r\gt1/4`$. Choose $`m=1`$. Monotonicity and the nonwrapping single-contact phase imply

```math
d_1^{\mathrm{wit}}(r)
\ge d_1^{\mathrm{wit}}(1/4)
\ge2c
\ge c\min\{1,Nr\}.
```

The middle inequality follows from the adjacent-pair lower bound at $`r=1/4`$ and $`\sin(\Phi_1/2)\ge\Phi_1/\pi`$.

All three cases establish the claimed uniform lower bound. For $`N=0`$, the limiting thermal and Markov free channels agree, so the corresponding distance is zero.

## 5. Small-memory behavior and finite-cutoff interpretation

For fixed $`m`$ and $`\beta/\tau\to0`$, the adjacent integral satisfies

```math
I_1(h)=\frac{\gamma\beta}{4}+o(\gamma\beta),
```

while the nonadjacent integrals are exponentially small in $`h/\beta`$. Hence

```math
\frac{\Phi_m}{m\gamma\beta}\longrightarrow1,
\qquad
d_m^{\mathrm{wit}}
\sim\frac{e^{-1}}{2}m\gamma\beta.
```

This fixed-$`m`$ asymptotic is distinct from the uniform bound above, which permits $`m`$ to grow as $`1/(\gamma\beta)`$.

At finite ultraviolet cutoff, the symmetric covariance is not exactly white: the witness modulus also changes. Its discrepancy must therefore be computed from the full complex coherence, rather than only from its phase. The [regularization analysis](regularization.md) proves convergence of the finite-contact process and gives an explicit error bound. It follows that a sufficiently large finite cutoff preserves a fixed fraction of the witness discrepancy while making the uncontrolled channels arbitrarily close to the target semigroup.

The [verification checks](../verification/README.md) compare a finite-oscillator matrix evolution with its exact influence factor and compare two independent finite-cutoff integral representations. They check normalization, history ordering, and cutoff conventions. They do not replace the all-temperature analytical proof.

## Prior result used

The positive-frequency free-semigroup/regression-failure mechanism is established in D. Lonigro and D. Chruściński, [*Quantum regression in dephasing phenomena*](https://arxiv.org/abs/2202.11056), J. Phys. A **55**, 225308 (2022), especially Proposition 3.2. The contribution proved here is the explicit protected-reference contact witness and its uniform quantitative lower bound. The repository's reference comparison gives the broader attribution and scope.
