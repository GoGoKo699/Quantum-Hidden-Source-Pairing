# How many shots does each measurement model need?

The [source model](model.md) supplies $`T`$ independent snapshots of an unknown perfect matching $`M`$ on $`m\ge4`$ labeled ports, where $`m`$ is even. Each port has dimension $`d\ge2`$. The states on true pairs are independent within a snapshot and have common known visibility $`0\lt \theta\le1`$. The decoder must output the entire matching with failure probability at most $`0\lt \delta\le1/4`$ for every $`M`$.

There are three measurement models. A joint decoder can measure all registers together. A port-local decoder can retain and process all $`T`$ specimens at each port and exchange classical messages. A specimen-separable measurement has effects separable over the $`mT`$ individual registers, a condition that includes adaptive procedures that measure and discard the specimens one at a time. The port-local decoder can couple shots at a single port, which can produce measurement effects entangled across its local time registers.

Let $`L=\log(m/\delta)`$. The lower bounds below combine with the [joint and local receivers](receiver.md) to give the following shot budgets, with uniform constants.

| Measurement model | Necessary shots | Sufficient shots |
| --- | --- | --- |
| Joint | $`\Omega(\theta^{-2}L)`$ | $`O(\theta^{-2}L)`$ |
| Specimen-separable effects | $`\Omega(d\theta^{-2}L)`$ | $`O(d\theta^{-2}L)`$ |
| Port-local operations and classical communication | $`\Omega(\max\{\theta^{-2},d/\theta\}\,L)`$ | $`O(d\theta^{-2}L)`$ |

At fixed positive visibility the last row is $`\Theta(dL)`$. Its dimension factor holds with arbitrary local temporal quantum memory. For visibility tending to zero, that row leaves a gap between the sufficient and necessary budgets.

## From information to exact recovery

Write $`\tau_k=I/d^k`$ and $`\rho_M`$ for the one-snapshot state. Under a uniformly drawn matching, let $`P_M`$ be the outcome law and $`\overline{P}`$ its mean. For any reference law $`Q`$, the average of $`D(P_M\|Q)`$ equals the mutual information of the matching and the outcome plus $`D(\overline{P}\|Q)`$. Use $`Q`$ from the same measurement on $`\tau_m^{\otimes T}`$. With $`N=(m-1)!!`$ possible matchings, Fano’s inequality implies

```math
\mathbb E_M D(P_M\|Q)\ge (1-\delta)\log N-\log 2.
```

Here and below logarithms in information quantities are natural. At $`m\ge4`$ and $`\delta\le1/4`$ the right-hand side is $`\Omega(m\log m)`$, including the three matchings at $`m=4`$. This yields the $`\log m`$ terms. The separate quartet arguments below yield the dependence on $`\log(1/\delta)`$ even when the number of ports stays fixed. Taking the larger of the two lower bounds gives their sum up to a factor of two.

## Unrestricted joint readout

On one true pair, the mixture $`\rho_\theta=(1-\theta)\tau_2+\theta(I+F)/(d(d+1))`$ and the reference $`\tau_2`$ are both constant on the symmetric and antisymmetric subspaces of the exchange operator $`F`$. Their quantum relative entropy equals a binary relative entropy

```math
D(\rho_\theta\|\tau_2)=D_{\rm Ber}(p_1\|p_0),
\qquad p_0=\frac{d+1}{2d},\qquad p_1=p_0+\theta(1-p_0).
```

The bound $`D_{\rm Ber}(u\|v)\le (u-v)^2/[v(1-v)]`$ gives $`D_{\rm Ber}(p_1\|p_0)\le\theta^2`$. After tensoring $`mT/2`$ independent pairs, data processing gives $`D(P_M\|Q)\le (mT/2)\theta^2`$ for every joint measurement. The preceding information bound now gives $`\Omega(\theta^{-2}\log m)`$.

For high confidence, choose two matchings that differ only on four ports. Write $`\sigma_0,\sigma_1`$ for the corresponding one-shot quartet states. Any estimator with failure $`\delta`$ on both matchings gives an equal-prior binary test with error at most $`\delta`$. The remaining ports have an identical state under both alternatives and can be prepared by the tester.

For $`\theta\le1/2`$, the density relative to the two-port maximally mixed state is $`I+\theta J`$, where $`J=(dF-I)/(d+1)`$ has operator norm at most one. Each quartet state is the product over two disjoint pairs. Therefore $`\sigma_1\succeq I/(4d^4)`$ and $`\|\sigma_0-\sigma_1\|_\infty\le5\theta/d^4`$. These give

```math
D(\sigma_0\|\sigma_1)
\le \log\mathrm{Tr}(\sigma_0^2\sigma_1^{-1})
\le \mathrm{Tr}\big[(\sigma_0-\sigma_1)^2\sigma_1^{-1}\big]
\le 100\theta^2.
```

The first inequality follows by applying Jensen’s inequality to $`\log(r_i/s_j)`$ with weights $`r_i|\langle i|j\rangle|^2`$ for eigenpairs of $`\sigma_0`$ and $`\sigma_1`$. The root fidelity $`f(\sigma_0,\sigma_1)=\|\sqrt{\sigma_0}\sqrt{\sigma_1}\|_1`$ satisfies $`f\ge\exp[-D(\sigma_0\|\sigma_1)/2]`$. Multiplicativity of $`f`$ and the trace-distance fidelity bound imply that the optimal test error is at least $`f^{2T}/4\ge e^{-100T\theta^2}/4`$.

For $`\theta\ge1/2`$, both quartet states dominate the common positive operator $`\Pi_{\rm sym}^{(4)}/d^4`$, where $`\Pi_{\rm sym}^{(4)}`$ projects onto the fully symmetric subspace of the four ports. Indeed, each exchange acts as $`+1`$ there, and both states have eigenvalue at least $`1/d^4`$ there. This common operator has trace at least $`1/24`$. The two $`T`$-shot states then share a positive component of trace at least $`24^{-T}`$, so every equal-prior test errs with probability at least $`24^{-T}/2`$. This also implies the bound $`e^{-100T\theta^2}/4`$ in this visibility range. Together the two cases give $`T\ge (100\theta^2)^{-1}\log(1/(4\delta))`$. Combining this with the matching-count term gives $`\Omega(\theta^{-2}L)`$.

## Sharp information loss for specimen-separable effects

It suffices to refine each separable outcome into product positive effects. Refining can only increase either relative entropy. Zero effects can be dropped. For one refined outcome $`y`$, normalize the local factors to trace-one operators $`\sigma_{y,i}`$, with $`i`$ indexing individual specimens. Let $`\mathcal E_M`$ be the set of $`R=mT/2`$ true pairs across the batch. For a pair $`e=(i,j)`$, put $`t_e=\mathrm{Tr}(\sigma_{y,i}\sigma_{y,j})\in[0,1]`$. The likelihood relative to $`Q`$ factorizes:

```math
\frac{P_M(y)}{Q(y)}=\prod_{e\in\mathcal E_M}\ell(t_e),
\qquad
\ell(t)=1-\frac{\theta}{d+1}+\frac{\theta d}{d+1}t.
```

The outcome variables $`t_e`$ can be dependent. Their disjoint-edge product moments are nonetheless fixed. For any subset $`S\subseteq\mathcal E_M`$, the identity $`\mathrm{Tr}[(A\otimes B)F]=\mathrm{Tr}(AB)`$ and POVM completeness give

```math
\mathbb E_Q \prod_{e\in S}t_e
=\frac{1}{d^{mT}}\mathrm{Tr}\prod_{e\in S}F_e
=d^{-|S|}.
```

Thus the expectation under $`Q`$ of any polynomial affine in each coordinate equals its evaluation at all coordinates $`1/d`$. The same expectations hold if every $`t_e`$ is replaced by an independent Bernoulli variable of mean $`1/d`$.

For the forward divergence, expand the log likelihood and use the chord from $`t=0`$ to $`t=1`$ to upper-bound the convex function $`\ell(t)\log\ell(t)`$ in each term. Each summand is this function for one edge times the nonnegative factor $`\prod_{e'\ne e}\ell(t_{e'})`$. The resulting polynomial is affine in every coordinate, so its expectation is the independent Bernoulli one. For the reverse divergence, apply the same chord construction to the convex function $`-\log\ell(t)`$ in each term. Write $`q_0=1/d`$ and $`q_1=q_0\ell(1)=q_0+\theta(d-1)/(d(d+1))`$. The endpoint variable has probability $`q_0`$ of one under the reference, and reweighting by $`\ell`$ changes that probability to $`q_1`$. This gives both bounds

```math
D(P_M\|Q)\le R\,D_{\rm Ber}(q_1\|q_0),\qquad
D(Q\|P_M)\le R\,D_{\rm Ber}(q_0\|q_1).
```

Measuring each port in the same orthonormal basis achieves equality in the two bounds against the specified reference. The local factors are then basis projectors so every $`t_e`$ is a collision indicator, and the chord inequalities are equalities. The optimality here concerns relative entropy against the reference for a fixed matching and specimen-separable effects.

Both binary divergences are $`O(\theta^2/d)`$. For instance, $`q_1-q_0\le\theta/d`$, $`q_1\ge q_0`$, and $`1-q_1\ge1/3`$, so the binary relative entropy bound used above applies to both directions. The forward inequality and Fano’s inequality yield $`\Omega(d\theta^{-2}\log m)`$.

For confidence, again use two matchings differing on a quartet. The restrictions to the quartet of the original POVM, obtained by supplying the common outside state, are specimen-separable. In the product expansion of an effect, each outside factor contributes only a nonnegative scalar when contracted with that state. Let $`A_0,A_1`$ be the disjoint outcome events for outputting the two exact matchings. Against the quartet maximally mixed reference there is a $`b\in\{0,1\}`$ with $`Q(A_b)\le1/2`$. The true outcome law has $`P_b(A_b^c)\le\delta`$. Binary data processing and the reverse bound with $`R=2T`$ give

```math
\frac12\log(1/\delta)-\log 2
\le D(Q\|P_b)
\le 2T D_{\rm Ber}(q_0\|q_1).
```

The left side follows from $`Q(A_b^c)\ge1/2`$ and the binary entropy bound $`\log 2`$. The reverse divergence is useful because the accuracy demand controls errors under $`P_b`$ while the reference remains common to both matchings. Combining with the matching-count term establishes $`\Omega(d\theta^{-2}L)`$.

## Temporal memory within every port

The next lower bound holds even when each port stores all of its specimens and can perform arbitrary local instruments with two-way classical communication. It also holds for effects positive under partial transpose (PPT) across one fixed cut of the ports used in the proof. Each port is placed wholly on one side of the cut, including its full time sequence. Assume no preshared inter-port entanglement or inter-port quantum communication in the port-local model.

Make $`K=\lfloor m/4\rfloor`$ disjoint quartets and place two ports of each quartet on each side of the cut. Choose the two possible cross-cut perfect matchings of each quartet independently with probability $`1/2`$. Fix an extra pair if two ports remain. For an effect $`E_y`$ and a state $`\rho`$, partial transpose of every register on the second side preserves the pairing $`\mathrm{Tr}(E_y\rho)=\mathrm{Tr}(E_y^{\Gamma}\rho^{\Gamma})`$. The transposed effects form a POVM because the original effects are PPT and sum to identity. The physical states on all cross-cut pairs also remain positive after this transpose. Specifically, $`F^{\Gamma}=d\Phi`$, with $`\Phi`$ the normalized maximally entangled projector, gives

```math
\rho_\theta^{\Gamma}=(1-\epsilon)\tau_2+\epsilon\Phi,
\qquad \epsilon=\frac{\theta}{d+1}.
```

We can bound the performance of any receiver on the transposed states by giving it additional classical information. Prepare each transposed pair as the mixture above using an independent Bernoulli flag, and reveal for each quartet whether any of its $`2T`$ flags were positive. If so, also reveal its matching bit. A quartet with no positive flags is entirely maximally mixed, so its bit is still uniform and independent of everything delivered to the receiver. Therefore even this assisted decoder has exact recovery probability at most

```math
\left[1-\tfrac12(1-\epsilon)^{2T}\right]^K.
```

The calculation bounds the original PPT measurement because the marginal transposed states are available to the assisted decoder, which can run the same measurement with the extra information discarded.

Since minimax success $`1-\delta`$ implies the same average success on this input family, the finite inequality implies

```math
T\ge
\frac{\log\big(K/[2(-\log(1-\delta))]\big)}{-2\log(1-\epsilon)}
=\Omega\!\left(\frac{d}{\theta}\log(m/\delta)\right).
```

The scaling uses $`\epsilon\le1/3`$, $`\delta\le1/4`$, and $`K\ge m/6`$ for the allowed even values of $`m`$. Combining with the unrestricted joint lower bound yields the necessary budget in the port-local row. At fixed positive visibility the common-basis receiver matches this order. The weak-visibility gap concerns the ability to couple shots locally, a resource absent from the sharper specimen-separable proof.
