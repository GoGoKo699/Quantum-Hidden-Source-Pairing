# The receivers

Each shot supplies one register from each of $`m`$ labeled ports. The hidden links form a fixed perfect matching. Write $`d=2^n`$ for the dimension of a port, $`\theta\in(0,1]`$ for the known visibility, $`T`$ for the number of shots, and $`\delta`$ for the target probability of an incorrect matching. The [source model](model.md) gives the sampled states and makes the port and shot labels explicit.

## Coherent threshold exchange

On two port registers let $`F`$ be their exchange operator and $`\Pi_+=(I+F)/2`$ the projector onto the symmetric subspace. A matched pair has joint state $`\rho_\theta=(1-\theta)I/d^2+\theta(I+F)/[d(d+1)]`$. For an unmatched pair the two-register state is $`I/d^2`$. Thus the two success probabilities for a symmetric outcome are

```math
p_0=\frac{d+1}{2d},\qquad
p_1=p_0+\theta(1-p_0).
```

For a candidate link $`e`$, the $`T`$ exchange operators $`F_{e,t}`$ commute because they act on different shots. The symmetric count operator is $`N_e=\sum_{t=1}^T(I+F_{e,t})/2`$. Set $`a=(p_0+p_1)/2`$. Define the candidate test by the two projectors

```math
E_e=\mathbf 1\{N_e/T\ge a\},\qquad I-E_e.
```

The receiver measures these two outcomes for every candidate link in a predetermined order, reusing the same data. It outputs the set of accepted links if this set is a perfect matching. Otherwise it reports failure. Each test implements the projective state update associated with its reported threshold bit. This state update is essential because successive tests can share a port.

### Circuit

1. Buffer the $`T`$ shots. Initialize a binary counter and a sign work qubit to zero.
2. For shot $`t`$, write the sign of $`F_{e,t}`$ into the work qubit with Hadamard, controlled exchange, Hadamard. The work bit is $`0`$ on the symmetric subspace and $`1`$ on the antisymmetric subspace. Increment the counter when this bit is $`0`$. Apply the same sign circuit again to clear the bit.
3. Copy the predicate `count / T >= a` to a fresh flag. The reversible comparator uses the integer threshold $`\lceil Ta\rceil`$.
4. Reverse the count circuit. Measuring only the flag now performs the two-outcome projective test. Clear the flag using its measured value and move to the next link.

The counter equals a function of the exchange eigenvalues on their common eigenspaces. Reversing the calculation clears every work register other than the flag and leaves the data coherent within each threshold subspace. Reading the individual exchange signs would implement a finer measurement with a different state update.

### Probability of recovering the wiring

On the original $`T`$-shot state of a fixed matching, the distribution of $`N_e`$ is binomial with parameter $`p_1`$ for a true edge and $`p_0`$ otherwise. For a fixed edge let $`C_e`$ be its correct-outcome projector, either $`E_e`$ or $`I-E_e`$. The Hoeffding bound gives

```math
1-\operatorname{Tr}(C_e\rho)\le
\exp\!\left[-\frac{T(p_1-p_0)^2}{2}\right].
```

Here $`\rho`$ is the buffered state before the first candidate test. The edge tests can disturb one another. [Gao's quantum union bound](https://arxiv.org/abs/1410.5688) bounds the probability of seeing any incorrect outcome in the actual sequence by four times the sum of the individual failure probabilities on $`\rho`$. With $`K=\binom m2`$, it suffices to take

```math
T\ge\frac{8d^2}{\theta^2(d-1)^2}\log\frac{4K}{\delta}.
```

This is $`O(\theta^{-2}\log(m/\delta))`$ for $`d\ge2`$. The same proof uses any supplied lower bound on visibility in the threshold and shot budget. The measurements remain valid if an edge's true visibility is larger.

At $`\theta=1`$, the simpler projector $`E_e=\prod_{t=1}^T(I+F_{e,t})/2`$ accepts a true link with certainty on the original input. Its false acceptance probability there is $`p_0^T`$. Four qubit ports have six candidate links, two true and four false. The all-symmetric test gives a failure bound of $`16(3/4)^T`$. For example, $`T=21`$ bounds the failure probability by $`0.0381`$.

### Gate and storage costs

The receiver takes $`mT`$ native specimens and holds $`mTn`$ data qubits. The reusable counter and work qubits take $`O(\log(T+1))`$ additional qubits. The circuit uses four controlled register exchanges per shot per candidate in this counter implementation. A controlled $`n`$-qubit register exchange decomposes into $`n`$ controlled qubit swaps. Reversible counting contributes $`O(T\log(T+1))`$ elementary gates per candidate using ripple increments with reusable work bits. The total is $`O(m^2T[n+\log(T+1)])`$ gates with direct connectivity. Geometry, idle errors during buffering, and gate calibration are separate implementation costs.

## One shot in quantum memory

One can exchange temporal storage for more specimens. Decompose the candidate graph on the $`m`$ ports into $`m-1`$ rounds of disjoint edges by the round-robin schedule. To construct it, fix one port and rotate the other $`m-1`$ port labels around a circle. In each round pair the fixed port with the first label and pair remaining labels at opposite offsets from that label. Each pair appears exactly once over the schedule.

For one round, repeat ordinary exchange-sign measurements on its disjoint pairs for $`T_0`$ fresh shots. Accumulate the corresponding symmetric counts in classical memory and use the same midpoint threshold before moving to the next round. All the scheduled tests of a shot are on disjoint registers. A classical union bound with the preceding per-edge Hoeffding estimate suffices for

```math
T_0\ge\frac{8d^2}{\theta^2(d-1)^2}\log\frac{K}{\delta}.
```

The method uses $`(m-1)T_0`$ shots and buffers a single $`mn`$-qubit snapshot at a time. It uses $`KT_0`$ controlled register exchanges if the pair measurements are done with the one-bit exchange circuit. It still needs cross-port gates. This schedule is an explicit memory–shot point. Its cost does not establish optimality when the receiver has a bounded cross-shot buffer.

## A port-local receiver

Measure every port in the same fixed basis on each shot. Each candidate edge gets an equality bit for the two observed basis labels. The success probabilities on a false edge and a true edge are respectively

```math
q_0=\frac1d,\qquad
q_1=\frac1d+\frac{\theta(d-1)}{d(d+1)}.
```

The formula uses $`\langle ii|F|ii\rangle=1`$ and the number of diagonal outcomes of the form $`(i,i)`$. An ordinary basis read at every port supplies all edge statistics from the same shots. Threshold each edge midway between the two means, and output the accepted links if they form a perfect matching.

The half-gap is at least $`\theta/(6d)`$. The Bernoulli variance for either edge type is at most $`2/d`$, and the half-gap is at most $`1/(2d)`$. Bernstein's inequality therefore bounds an edge error by $`\exp[-T\theta^2/(180d)]`$. A union bound over $`K`$ candidates ensures error at most $`\delta`$ for

```math
T\ge 180d\theta^{-2}\log\frac{K}{\delta}.
```

The basis can be the computational basis, so this receiver needs single-qubit measurements, an agreement on basis convention, and classical comparison and counting. It has no temporal quantum storage and uses $`mT`$ native specimens. The [converse](bounds.md) compares the shot count to arbitrary specimen-separable measurements and, at fixed positive visibility, to the broader class with coherent time storage separately at each port.

The [verification checks](../verification/README.md) evaluate the measurement probabilities and state updates on small instances with exact arithmetic.
