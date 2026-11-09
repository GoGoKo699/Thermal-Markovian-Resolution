# What the thermal contact law means

The [main theorem](model.md#3-main-theorem) concerns the accuracy of one specified Markov description under control. Its central parameter is the product of the number of contacts, the dephasing rate and the inverse temperature. Three distinctions explain the result: fluctuations versus response, a free channel versus a controlled process, and a physical bandwidth approximation versus the thermal time.

## Fluctuations can be white while response retains memory

For a centered Gaussian bath, the symmetrized two-point function determines the loss of coherence. Exact all-time dephasing calibration makes that function white. Thermal detailed balance also relates the symmetric and antisymmetric parts of the spectrum. The latter therefore remains nonzero at finite temperature, even though it drops out of every uncontrolled channel.

The influence of two longitudinal histories $`a(t),b(t)\in\{-1,1\}`$ separates these two effects. With $`\delta=a-b`$ and $`\Sigma=a+b`$,

```math
F[a,b]=
\exp\!\left[
-\frac\gamma2\int_0^\tau\delta(t)^2\,dt
+i\int_{s\lt t}\delta(t)\Sigma(s)\eta_\beta(t-s)\,ds\,dt
\right].
```

The first term is exactly the Markov dephasing factor. For histories that are constant on the same interval, $`\delta\Sigma=a^2-b^2=0`$, so the response does not change that interval's uncontrolled channel. A contact can change the histories and leave a response contribution linking different intervals. This is the quantum regression failure described in the [prior literature](../references/RELATED_WORK.md), now quantified in a specified operational distance.

The lower witness uses this distinction directly. On one set of intervals the two reference branches drive the bath in the same way. On the next set they differ and read the response. A protected qubit retains coherence between these paths. The white-noise decay remains fixed, while the response phases accumulate with one sign. This establishes an attainable control-dependent discrepancy; it does not certify that every classical-memory explanation of the process is impossible.

## A limit on every scheduled tester

Detecting a phase with a chosen pulse sequence supplies a lower bound on distinguishability. The operational upper makes the complementary statement: no permitted tester, regardless of its protected-memory dimension or recorded feedback operations, can produce a larger order of discrepancy when $`N\gamma\beta`$ is small.

For each contact, the total response crossing its time is bounded by the first positive-time response moment. Summing these contributions and using norm-one insertions in the complete circuit produces the upper bound. The method credits established Gaussian stability estimates and earlier contact-counting geometry; its application to the imaginary response is justified in the [proof](operational_bound.md).

Together, the upper and witness turn a selected regression counterexample into an optimal contact budget for this calibrated class. A large contact allowance permits an effective witness; it does not force every chosen sequence to reveal memory. A poorly chosen measurement can remain insensitive.

In the regime $`\gamma\beta\ll1`$, obtaining any fixed target discrepancy $`0\lt\delta\le c`$, with $`c`$ as in the main theorem, requires and permits

```math
N=\Theta\!\left(\frac1{\gamma\beta}\right).
```

At the fixed horizon $`\tau=1/\gamma`$, the corresponding average contact spacing is of order $`\beta`$. Restoring units identifies this time as $`\hbar/(k_B T_{\rm bath})`$. The thermal timescale is familiar; the result determines its role after optimizing over the entire stated tester class. It does not provide a repetition-cost law for estimating an unknown temperature or detecting arbitrarily small biases.

## Increasing bandwidth leaves a distinct thermal limit

Finite bandwidth changes the symmetric fluctuations as well as the response. The [cutoff theorem](regularization.md) controls both effects. For fixed contact budget and finite temperature, the explicit cutoff family approaches the same limiting thermal process. Its uncontrolled-channel error tends to zero, but its optimized controlled discrepancy approaches a quantity bounded below by the thermal contact law.

This differs from a bounded-interaction survival or Zeno obstruction. Such an obstruction can become weaker as the interaction bound is increased. Here the remaining response is imposed by KMS detailed balance together with exact all-time calibration. The [autonomous-noise comparator](../references/RELATED_WORK.md) uses commuting nonthermal fields, so the thermal premise is absent there.

The physical statement is constructive and precisely limited: the displayed finite-cutoff approximants retain the discrepancy. It does not imply that every finite-cutoff bath giving a good experimental semigroup fit has the same lower bound. Establishing such a statement would require a new stability or minimax theorem for approximate calibration.

## Why calibration scope and preparation matter

All-time equality identifies the symmetrized spectrum by Fourier uniqueness, and KMS fixes the response. A finite window does not identify the same spectrum: the [explicit perturbation](calibration.md) changes its cosine transform outside the measured window while preserving the free channel inside it. A finite number of observations is weaker still. Thus the theorem describes a mathematically specified calibration class, not a data-only certification rule.

The bath starts in equilibrium for its free Hamiltonian before the probe–bath evolution. A global interacting Gibbs preparation would change the initial correlations and the meaning of allowed probe preparations. It is a different problem. Similarly, varying temperature while keeping one experimental spectrum fixed generally changes the free decay; the present family retunes the spectrum to retain the same target rate.

Finally, the contact count leaves control duration and work uncharged. Finite-cutoff Hamiltonians are physically semibounded, but the associated reorganization energy can grow with cutoff. The theorem should therefore be used as a contact-resource statement, with its initial preparation and spectral calibration made explicit.
