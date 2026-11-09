# Ultraviolet regularization and physical approximations

The thermal process is defined by a limit of finite-cutoff models. This page proves that the limit exists for every finite contact schedule and gives a cutoff error bound that is uniform over the allowed instruments, protected memory, and contact positions.

Throughout, $`0\lt\beta\lt\infty`$, $`\gamma\gt0`$, and the headline observation horizon is $`\tau=1/\gamma`$. Let $`\mathcal P_{\beta,\Omega}`$ denote the process with spectral density

```math
J_{\beta,\Omega}(\omega)
=\frac{\gamma}{\pi}\tanh\!\left(\frac{\beta\omega}{2}\right)
\mathbf 1_{(0,\Omega]}(\omega).
\tag{1}
```

Let $`\mathcal P_\beta`$ be its infinite-cutoff finite-contact limit and $`\mathcal M_\gamma`$ the Markov dephasing process. The distance $`d_N`$ is the supremum final half trace distance over testers with at most $`N`$ preassigned interior contact times, with every outcome retained as specified in [the model](model.md).

## 1. Cutoff theorem

Put $`L=N+1`$ and define

```math
S_\Omega=\frac{16\gamma L^2}{\pi\Omega},
\qquad
\varepsilon_\Omega
=\min\!\left\{1,\frac{e^{S_\Omega}-1}{2}\right\}.
\tag{2}
```

Then

```math
\boxed{
d_N(\mathcal P_{\beta,\Omega},\mathcal P_\beta)
\le \varepsilon_\Omega .
}
\tag{3}
```

The estimate is uniform in finite protected-memory dimension, all permitted instruments and feedforward operations at the fixed times, and the choice of those times. It does not cover outcome-dependent choices of the contact times. The parameter $`\Omega`$ bounds oscillator mode frequencies; it is not a bound on the spectral diameter of the full oscillator Hamiltonian or on the interaction norm.

The uncontrolled coherence is $`e^{-\Gamma_\Omega(t)}`$, where

```math
\Gamma_\Omega(t)
=\frac{4\gamma}{\pi}
\int_0^\Omega\frac{1-\cos(\omega t)}{\omega^2}\,d\omega.
\tag{4}
```

For every $`t\ge0`$,

```math
0\le 2\gamma t-\Gamma_\Omega(t)
\le\frac{8\gamma}{\pi\Omega}.
\tag{5}
```

Consequently all free channels converge uniformly in time to the same dephasing semigroup, while the controlled process approaches $`\mathcal P_\beta`$, whose distance from $`\mathcal M_\gamma`$ need not vanish. These are sufficient cutoff estimates; no optimal bandwidth or finite-bath resource law is asserted.

## 2. Finite-cutoff Hamiltonians are semibounded

For clarity, first use the bosonic Fock representation over $`L^2((0,\Omega),d\omega)`$. Let $`H_B=d\Gamma(\omega)`$, choose a form factor satisfying $`|g(\omega)|^2=J_{\beta,\Omega}(\omega)`$, and write

```math
B=a(g)+a^\dagger(g),
\qquad
H=I_S\otimes H_B+Z\otimes B.
\tag{6}
```

Both

```math
\|g\|^2=\int_0^\Omega J_\beta(\omega)\,d\omega
\lt\infty,
\qquad
E_\Omega
:=\left\|\frac{g}{\sqrt\omega}\right\|^2
=\int_0^\Omega\frac{J_\beta(\omega)}{\omega}\,d\omega
\lt\infty
\tag{7}
```

hold. At the infrared endpoint,

```math
J_\beta(\omega)
=\frac{\gamma\beta}{2\pi}\omega+O(\omega^3),
\tag{8}
```

and the ultraviolet endpoint is finite by construction.

For a unit vector $`\psi`$ in the quadratic-form domain of $`H_B`$, the annihilation-operator estimate gives

```math
\|a(g)\psi\|
\le \sqrt{E_\Omega}\,\|H_B^{1/2}\psi\|.
\tag{9}
```

Thus

```math
\begin{aligned}
|\langle\psi,B\psi\rangle|
&\le2\sqrt{E_\Omega}
       \sqrt{\langle\psi,H_B\psi\rangle},\\
\langle\psi,(H_B\pm B)\psi\rangle
&\ge
\langle H_B\rangle
-2\sqrt{E_\Omega\langle H_B\rangle}
\ge-E_\Omega.
\end{aligned}
\tag{10}
```

More generally, for every $`\epsilon\gt0`$,

```math
|\langle\psi,B\psi\rangle|
\le\epsilon\langle\psi,H_B\psi\rangle
+\frac{E_\Omega}{\epsilon}\|\psi\|^2.
\tag{11}
```

The linear field is therefore infinitesimally form bounded relative to $`H_B`$. The KLMN theorem and the representation theorem for closed forms define self-adjoint conditional Hamiltonians $`H_B+B`$ and $`H_B-B`$, each bounded below by $`-E_\Omega`$; see [Simon, Theorems 10.5 and 10.8](https://doi.org/10.1007/s13373-018-0118-0). Their direct sum is the qubit-bath Hamiltonian. Adding the common scalar $`E_\Omega I`$ makes it nonnegative and changes no measured probabilities.

This argument does not require $`g/\omega`$ to be square integrable. In fact, that stronger condition fails logarithmically at zero frequency for (1). A normalizable displaced Fock vacuum or a Fock-space polaron unitary is not implied by semiboundedness.

## 3. What the thermal preparation means

The initial bath is Gaussian and KMS at inverse temperature $`\beta`$ for the **free** Hamiltonian $`H_B`$, independently of the probe and its protected memory. Its covariance convention is

```math
\begin{aligned}
C_{\beta,\Omega}(u)
&=\langle B(u)B(0)\rangle_\beta\\
&=\int_0^\Omega J_\beta(\omega)
\left[
 \coth\!\left(\frac{\beta\omega}{2}\right)\cos(\omega u)
 -i\sin(\omega u)
\right]\,d\omega\\
&=\frac{\gamma}{\pi}\int_0^\Omega\cos(\omega u)\,d\omega
-i\int_0^\Omega J_\beta(\omega)\sin(\omega u)\,d\omega.
\end{aligned}
\tag{12}
```

This is a product preparation followed by interacting evolution. It is not a global Gibbs state of (6).

In a continuum, a KMS state need not be a trace-class density matrix on the vacuum Fock representation used in Section 2. The covariance in (12) defines the Gaussian bath expectations needed here. Section 8 also constructs finite-mode approximations with ordinary normalized Gibbs density matrices, providing a concrete route to the same finite-contact process.

The finite-cutoff equal-time variance is finite:

```math
\langle B^2\rangle_\beta
=\frac{\gamma\Omega}{\pi}.
\tag{13}
```

The Fock-space semiboundedness statement and the existence of the thermal Gaussian functional are distinct statements; no positive thermal GNS Liouvillian is being asserted.

## 4. Integrated coefficients and the ultraviolet tail

Fix a schedule

```math
0=t_0\lt t_1\lt\cdots\lt t_L=\tau,
\qquad
I_j=(t_{j-1},t_j),
\qquad
h_j=t_j-t_{j-1}.
\tag{14}
```

Coincident contacts may be composed before defining this partition. Set

```math
f_j(\omega)=\int_{I_j}e^{i\omega t}\,dt,
\qquad
|f_j(\omega)|\le\min\!\left\{h_j,\frac2\omega\right\}.
\tag{15}
```

Write $`R_{\beta,\Omega}=\operatorname{Re}C_{\beta,\Omega}`$ and $`\eta_{\beta,\Omega}=-\operatorname{Im}C_{\beta,\Omega}`$. The coefficients entering the exact Gaussian history influence are

```math
R_{jk}^{\Omega}
=\int_{I_j}dt\int_{I_k}ds\,R_{\beta,\Omega}(t-s)
=\frac{\gamma}{\pi}\int_0^\Omega
\operatorname{Re}[f_j(\omega)\overline{f_k(\omega)}]\,d\omega,
\tag{16}
```

and, for $`j\gt k`$,

```math
\eta_{jk}^{\Omega}
=\int_{I_j}dt\int_{I_k}ds\,\eta_{\beta,\Omega}(t-s)
=\int_0^\Omega J_\beta(\omega)
\operatorname{Im}[f_j(\omega)\overline{f_k(\omega)}]\,d\omega.
\tag{17}
```

For $`\Omega=\infty`$, these are finite and satisfy

```math
R_{jk}^{\infty}=\gamma h_j\delta_{jk},
\qquad
\eta_{jk}^{\infty}
=\int_{I_j}dt\int_{I_k}ds\,
\frac{\gamma}{\beta}
\operatorname{csch}\!\left(\frac{\pi(t-s)}{\beta}\right).
\tag{18}
```

The cross-interval integral remains finite even for adjacent intervals: at positive lag $`u`$, the measure of pairs straddling their common boundary is at most $`u`$, cancelling the response's $`1/u`$ short-lag singularity. Its spectral form in (17) is absolutely convergent at large frequency by (15).

Let $`\Delta R_{jk}=R_{jk}^{\Omega}-R_{jk}^{\infty}`$ and $`\Delta\eta_{jk}=\eta_{jk}^{\Omega}-\eta_{jk}^{\infty}`$. Since $`0\le J_\beta\le\gamma/\pi`$,

```math
\begin{aligned}
|\Delta R_{jk}|,\ |\Delta\eta_{jk}|
&\le \frac{\gamma}{\pi}
\int_\Omega^\infty |f_j(\omega)f_k(\omega)|\,d\omega\\
&\le\frac{4\gamma}{\pi}
\int_\Omega^\infty\frac{d\omega}{\omega^2}
=\frac{4\gamma}{\pi\Omega}
=:a_\Omega.
\end{aligned}
\tag{19}
```

For forward and backward histories $`a_j,b_j\in\{+1,-1\}`$, put $`\delta_j=a_j-b_j`$ and $`\Sigma_j=a_j+b_j`$. Their exact influence is

```math
F_\Omega(a,b)=
\exp\!\left[
-\frac12\sum_{j,k}\delta_j\delta_kR_{jk}^{\Omega}
+i\sum_{j\gt k}\delta_j\Sigma_k\eta_{jk}^{\Omega}
\right].
\tag{20}
```

There is no omitted response self-term: within one constant-history interval, $`\delta_j\Sigma_j=a_j^2-b_j^2=0`$. The exact Gaussian influence and response-phase mechanism have the antecedents discussed in [related work](../references/RELATED_WORK.md).

## 5. Existence and norm control of the limiting process

For a fixed partition, (19) makes every history coefficient in (20) converge. There are only $`4^L`$ forward/backward history pairs. For a fixed tester, its output is a linear combination of these coefficients and the corresponding ordered projector/instrument circuits.

Each bare history circuit has completely bounded trace norm at most one: left and right multiplication by a spectral projector are contractions, and complete tester instruments with their records retained are CPTP. Coefficient convergence therefore gives a completely bounded norm limit, uniformly over finite protected-memory dimension. Complete positivity and causal normalization of the uninserted process are preserved by this limit.

This finite-history argument establishes existence only. Its possible $`4^L`$ factor is not used in the quantitative bound (3).

For the sharper estimate, expand

```math
F_\Omega=F_\infty e^{\Delta Q},
\qquad
\Delta Q
=-\frac12\sum_{j,k}\Delta R_{jk}\delta_j\delta_k
+i\sum_{j\gt k}\Delta\eta_{jk}\delta_j\Sigma_k.
\tag{21}
```

Every product $`\delta_j\delta_k`$ or $`\delta_j\Sigma_k`$ has at most four signed monomials in the history variables. Multiplication by $`a_j`$ inserts left multiplication by $`Z`$ on the appropriate interval leg; multiplication by $`b_j`$ inserts right multiplication by $`Z`$.

For every finite physical approximation, such an inserted expression is an actual ordered system-bath circuit containing norm-one left/right $`Z`$ maps. Its completely bounded trace norm is at most one, even though an individual insertion need not preserve positivity. No insertion is moved across an instrument. Passing to the fixed-partition limit preserves this norm bound. Thus the same bound holds when the base influence in (21) is $`F_\infty`$.

The total absolute coefficient weight in $`\Delta Q`$ is bounded by

```math
\begin{aligned}
S_{\mathrm{actual}}
&\le
2\sum_{j,k}|\Delta R_{jk}|
+4\sum_{j\gt k}|\Delta\eta_{jk}|\\
&\le2L^2a_\Omega
+2L(L-1)a_\Omega\\
&\le4L^2a_\Omega
=\frac{16\gamma L^2}{\pi\Omega}
=S_\Omega.
\end{aligned}
\tag{22}
```

Summing the nonconstant exponential terms therefore gives

```math
\|\rho_\Omega^{\mathsf T}-\rho_\infty^{\mathsf T}\|_1
\le\sum_{q=1}^{\infty}\frac{S_\Omega^q}{q!}
=e^{S_\Omega}-1.
\tag{23}
```

Division by two, followed by the trivial bound one, proves (3). This is a specialization of established Gaussian perturbation and contractive-insertion methods, with the cancellation and coefficient estimates made explicit for this process.

## 6. Free evolution and a practical cutoff choice

For uninterrupted evolution, the two histories differ by two throughout the interval and the response phase vanishes. The resulting exponent is (4). The elementary identity

```math
\int_0^\infty\frac{1-\cos(\omega t)}{\omega^2}\,d\omega
=\frac{\pi t}{2},
\qquad t\ge0,
\tag{24}
```

and $`0\le1-\cos(\omega t)\le2`$ give (5).

The free dephasing channels have the same populations and real coherence multipliers. Their half diamond distance is one half the absolute difference of those multipliers. Consequently,

```math
\begin{aligned}
\frac12\|\mathcal E_{\Omega,t}-e^{t\mathcal L_\gamma}\|_\diamond
&=\frac12\left|e^{-\Gamma_\Omega(t)}-e^{-2\gamma t}\right|\\
&\le\frac12\left(1-e^{-8\gamma/(\pi\Omega)}\right)
\le\frac{4\gamma}{\pi\Omega}.
\end{aligned}
\tag{25}
```

For a requested process error $`0\lt\varepsilon\lt1`$, a sufficient cutoff is

```math
\Omega\ge
\frac{16\gamma(N+1)^2}
{\pi\log(1+2\varepsilon)}.
\tag{26}
```

This choice depends on the contact budget and accuracy but not on the tester. It is intentionally a sufficient estimate, not an optimized resource cost.

## 7. Persistence of the thermal discrepancy

Let $`x=N\gamma\beta`$ and let

```math
c=\frac{e^{-1}}{4\pi\sinh\pi}
\tag{27}
```

be the constant supplied by [the explicit witness](witness.md). The process triangle inequality yields

```math
d_N(\mathcal P_{\beta,\Omega},\mathcal M_\gamma)
\ge
\max\!\left\{0,\ c\min\{1,x\}-\varepsilon_\Omega\right\}.
\tag{28}
```

Expanding directly around the Markov influence, or combining the coefficient estimates, also gives

```math
d_N(\mathcal P_{\beta,\Omega},\mathcal M_\gamma)
\le
\min\!\left\{1,\frac{e^{x+S_\Omega}-1}{2}\right\}.
\tag{29}
```

The simpler triangle-inequality alternative, using the uniform limiting upper bound, is

```math
d_N(\mathcal P_{\beta,\Omega},\mathcal M_\gamma)
\le\min\{1,\ N\gamma\beta+\varepsilon_\Omega\}.
\tag{29a}
```

For example,

```math
\Omega\ge
\frac{16\gamma(N+1)^2}
{\pi\log\!\left(1+c\min\{1,N\gamma\beta\}\right)}
\tag{30}
```

ensures $`\varepsilon_\Omega\le(c/2)\min\{1,N\gamma\beta\}`$, so the finite-cutoff process retains at least half the stated limiting lower bound.

At fixed $`N\ge1`$ and fixed finite $`\beta\gt0`$, increasing $`\Omega`$ therefore makes all free channels arbitrarily accurate while preserving a nonzero controlled discrepancy. The statement concerns cutoff approximants of the exactly calibrated spectral family (1). It is not a universal lower bound over every bath satisfying only a finite-time or finite-tolerance free-calibration requirement.

## 8. Finite positive-frequency mode approximations

Fix finite $`\beta,\Omega,\tau`$. Divide $`[0,\Omega]`$ into finitely many bins $`A_\ell`$, choose $`\omega_\ell\in A_\ell\cap(0,\Omega]`$, and set

```math
w_\ell=\frac{\gamma}{\pi}|A_\ell|,
\qquad
|g_\ell|^2=w_\ell\tanh\!\left(\frac{\beta\omega_\ell}{2}\right).
\tag{31}
```

Use independent oscillators with

```math
H_B^{(m)}=\sum_{\ell=1}^{m}\omega_\ell b_\ell^\dagger b_\ell,
\qquad
B^{(m)}=\sum_{\ell=1}^{m}
\left(g_\ell b_\ell+\overline g_\ell b_\ell^\dagger\right),
\tag{32}
```

and the normalized product Gibbs state at the same $`\beta`$. Its covariance is

```math
C_m(u)=
\sum_{\ell=1}^{m}w_\ell
\left[
\cos(\omega_\ell u)
-i\tanh\!\left(\frac{\beta\omega_\ell}{2}\right)
\sin(\omega_\ell u)
\right].
\tag{33}
```

The integrands are jointly continuous on the compact frequency/time domain, including the combined thermal factors at zero frequency. Riemann sums therefore converge uniformly for $`|u|\le\tau`$ to (12). Define

```math
\epsilon_m=
\max\!\left\{
\sup_{|u|\le\tau}|\operatorname{Re}(C_m-C_{\beta,\Omega})(u)|,\quad
\sup_{|u|\le\tau}|\operatorname{Im}(C_m-C_{\beta,\Omega})(u)|
\right\}
\longrightarrow0.
\tag{34}
```

For any fixed finite partition, the coefficient differences obey

```math
|\Delta R_{jk}|,\ |\Delta\eta_{jk}|
\le\epsilon_m h_jh_k.
\tag{35}
```

The insertion estimate of Section 5 now has total weight

```math
\begin{aligned}
S_m
&\le2\epsilon_m\sum_{j,k}h_jh_k
+4\epsilon_m\sum_{j\gt k}h_jh_k\\
&\le4\epsilon_m\tau^2.
\end{aligned}
\tag{36}
```

Hence

```math
d_N(\mathcal P_{\beta,\Omega}^{(m)},\mathcal P_{\beta,\Omega})
\le
\min\!\left\{1,\frac{e^{4\epsilon_m\tau^2}-1}{2}\right\}.
\tag{37}
```

For each fixed finite contact budget, this convergence is uniform in its preassigned schedules and allowed tester memory, on the fixed horizon $`[0,\tau]`$. It is not an all-time approximation by one fixed finite-mode model. One may first establish the physical continuum process by the finite-history convergence argument and then apply the insertion estimate; there is no assumption of an infinite-volume thermal density matrix.

Each discrete model has positive mode frequencies, an ordinary Gibbs density matrix, and a semibounded longitudinal Hamiltonian. Combining (37) and (3) proves finite-mode existence at any prescribed finite-contact accuracy. Finite modes still have infinite-dimensional oscillator Hilbert spaces. This page does not give an occupation cutoff, an optimized number of modes, or a cost for bath preparation or control.

## 9. Limits of the Hamiltonian statement

As $`\Omega\to\infty`$, $`E_\Omega`$ grows logarithmically and the unsmeared linear field has divergent variance. At the formal endpoint $`\beta=\infty`$, the flat positive-frequency density also makes $`\int J(\omega)/\omega\,d\omega`$ diverge in the infrared. These facts are why the theorem keeps finite positive $`\beta`$ and defines the infinite-cutoff object through its finite-contact process.

They do not prove that a suitably renormalized ultraviolet Hamiltonian cannot exist. Such a construction is unnecessary for (3), (28), and the finite-mode approximation.

The contact budget does not bound control work, pulse duration, coupling strength, bath energy, or bandwidth. The common shift in Section 2 is dynamically irrelevant, but no uniform ultraviolet bound on control work follows from it. Finally, $`J_\beta`$ is retuned across temperatures to preserve the same free semigroup. Heating one fixed spectral density is a different comparison.
