# Learn the wiring from four ports

Imagine four labeled output ports. Two share one source and the other two share another, but you have no map of their connections. In each shot, each source chooses a new random pure state and prepares it twice, once for each of its ports. You receive four registers at known positions. The source’s choices are hidden. Your task is to identify the two links.

## A hidden label that survives a fresh draw

For this example, let the actual links be $`12`$ and $`34`$. The state at port 1 changes every shot. Its averaged density operator is $`I/d`$, where $`d`$ is the dimension of a register. The same holds at every other port. A separate stream from port 1 therefore carries no information about its partner.

The same-shot pair $`12`$ retains a relationship. Conditioned on a draw $`\lvert\psi\rangle`$, the two registers are in $`\lvert\psi\rangle\otimes\lvert\psi\rangle`$. Their order can be exchanged with no change in the vector. The operator $`F`$ that exchanges the register contents sends $`\lvert a\rangle\lvert b\rangle`$ to $`\lvert b\rangle\lvert a\rangle`$. The projectors $`P_+=(I+F)/2`$ and $`P_-=(I-F)/2`$ resolve its two eigenvalues.

Each hidden draw is independent of the draws on other links and shots. With isotropic draws, averaging the pair on a true link gives the normalized symmetric projector $`2P_+/[d(d+1)]`$. For a false link such as $`13`$, the states on the two ports are independent, so its average is $`I/d^2`$. A randomly chosen pair of independent pure states may still give the symmetric outcome. The probability is the fraction of the total pair Hilbert space belonging to that subspace.

## Read the links with a shared batch

Take one qubit at each port, so $`d=2`$. The symmetric subspace has dimension three, spanned by $`\lvert00\rangle`$, $`\lvert11\rangle`$, and $`(\lvert01\rangle+\lvert10\rangle)/\sqrt{2}`$. The antisymmetric subspace has dimension one. The noiseless experiment gives the following single-shot probabilities.

| Candidate pair | Probability of symmetric exchange | Probability of matching computational-basis outcomes |
|---|---:|---:|
| $`12`$ or $`34`$ | $`1`$ | $`2/3`$ |
| $`13,14,23,24`$ | $`3/4`$ | $`1/2`$ |

For instance, measuring the two true-link qubits locally in the computational basis checks for equality of two random outcomes. Two of the three symmetric basis vectors give equality, so the probability is $`2/3`$. The antisymmetric basis vector always gives unequal outcomes, as does the symmetric vector with one excitation. The exchange measurement separates the signs of those two superpositions.

A joint receiver buffers $`T`$ shots. For one candidate link it tests whether every corresponding pair is symmetric. In the buffered state, a true link passes certainly and a false link passes with probability $`(3/4)^T`$. The receiver makes only one projective decision per candidate. It computes the individual exchange signs coherently, copies the all-symmetric decision to an output qubit, and uncomputes the signs. That procedure leaves just the projected state on which the next candidate is tested.

The six decisions use the same data. For example, the tests for $`12`$ and $`13`$ act on shared registers, and their projectors need not commute. Gao’s quantum union bound controls the actual sequence by four times the sum of its original-state error probabilities. For this toy experiment, the probability of any wrong link decision is at most

```math
4\left(4\,(3/4)^T\right)=16(3/4)^T.
```

With $`T=21`$, this bound is about $`0.0381`$. Thus 21 snapshots, or 84 emitted qubits in this example, suffice for a guaranteed success probability of at least $`0.95`$. This is a sufficient count from the bound. The projective receiver and resource counts are detailed in the [receiver chapter](../science/receiver.md).

## Why a wider port changes the comparison

Keep the same wiring and make each register larger. In one shot, the symmetry outcome on an unrelated pair then has probability $`(d+1)/(2d)`$ and approaches $`1/2`$ as $`d`$ grows. A true link continues to pass the noiseless exchange test with probability one.

For common-basis measurements, unrelated ports agree with probability $`1/d`$. True partners agree with probability $`2/(d+1)`$, which also becomes small. The local learner needs enough of these rare equality events to distinguish the two rates. The [shot lower bounds](../science/bounds.md) explain why even local quantum memory across all shots and unlimited classical communication cannot remove the factor $`d`$ at fixed positive visibility. The argument turns independent four-port groups into independent hidden wiring bits and bounds how often the receiver can learn each bit.

## If the source sometimes misses a shared draw

Visibility $`\theta`$ is the probability of using the shared draw on a true link. At $`\theta=1/2`$ in the qubit example, a true link passes the exchange test in a single shot with probability $`7/8`$ and a false link with probability $`3/4`$. Looking for exchange symmetry in *every* shot would eventually reject true links too. The receiver instead coherently compares the fraction of symmetric outcomes to the midpoint $`13/16`$. More shots are needed to resolve this narrower gap.

For known $`0\lt \theta\le1`$ and failure allowance $`0\lt \delta\le1/4`$, the joint optimum scales as $`\theta^{-2}\log(m/\delta)`$. The optimum for effects separable over individual specimens has an extra factor $`d`$. The stronger port-local model permits coherent processing over all shots at any one port. There the extra factor $`d`$ is sharp at fixed positive visibility, while the optimal weak-visibility dependence remains open in this account.

The advantage is in the number of supplied snapshots. The joint implementation needs coherent storage and exchanges between ports. The [Watrous bridge](WATROUS_BRIDGE.md) prepares the mathematical tools and the [milestone map](MILESTONES.md) follows the proof and the access comparison in detail.
