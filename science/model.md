# Hidden source pairing

Suppose a device emits one quantum register at each labeled port on every clock cycle. Each source feeds exactly two ports. It changes its preparation on the next cycle, so a port's history by itself carries no information about which source feeds it. The task is to recover the wiring from the joint statistics of synchronous shots.

## The snapshot model

There are an even number $`m\ge 4`$ of ports of common dimension $`d\ge 2`$. For the qubit circuit, $`d=2^n`$. An unknown perfect matching $`M`$ of the port labels remains fixed. In each shot, independently for each link, draw one pure state and send it to both endpoints with probability $`\theta`$. With probability $`1-\theta`$, use independent draws at the two endpoints. Each draw is Haar on the local state space or from an exact complex projective 2-design. Every realized snapshot is a product across ports. The same preparation at two ports comes from a source with two outputs, so the model does not invoke cloning of a received specimen.

Write $`F_{ij}`$ for the register exchange, $`\tau=I/d`$ for the state of one maximally mixed port, and $`\rho_\theta`$ for a matched pair's averaged state. The Haar second moment is the symmetric projector divided by its rank. Thus

```math
\rho_\theta = (1-\theta)\tau^{\otimes 2}+
\theta\frac{I+F}{d(d+1)},\qquad
\rho_M=\bigotimes_{(i,j)\in M}(\rho_\theta)_{ij}.
```

An unmatched pair's marginal is $`\tau^{\otimes 2}`$, and every port marginal is $`\tau`$. One physical realization of the same $`\rho_\theta`$ starts with shared pure draws and sends each through an independent whole-register depolarizing channel of retention $`\lambda`$. The resulting visibility is $`\theta=\lambda^2`$. The model uses ideal shot timing and readout. Per-qubit noise on a multiqubit register could change the visibility model and is a separate resource assumption.

The learner receives only the native registers, their port labels, and shot boundaries. It knows $`m,d,\theta`$, where $`0\lt \theta\le1`$. It receives no source seeds, state descriptions, preparation access, or extra copies of the latent draw. At $`\theta=0`$ the matching is unidentifiable. The state-design choice matters. Uniform multiqubit stabilizer states realize this exact pair model with polynomial-time state preparation at each endpoint. The proof makes no claim for product designs applied independently to the qubits within a port. [Design reference](../references/RELATED_WORK.md)

## Success and measurement access

A run succeeds only when its classical output is the entire true perfect matching. Require success at least $`1-\delta`$ for every matching, with $`0\lt \delta\le1/4`$. One shot supplies one register at each port, so $`T`$ shots use $`mT`$ physical specimens under every access model. The same shot and visibility conventions apply to these three classes.

| Measurement class | Allowed quantum processing |
| --- | --- |
| Joint | Arbitrary processing of the registers from all ports and shots. |
| Port-local | Arbitrary coherent processing within each port's full time sequence, local ancillas, and classical communication among ports. No inter-port quantum channel or supplied shared entanglement. |
| Specimen-separable | POVM effects separable over all individual port-shot registers. This includes adaptive destructive individual-specimen measurements and can be broader than their physical implementation. |

Port-local experiments need not be specimen-separable because a port may entangle its own time registers. A separate converse covers even POVMs whose effects are positive under partial transpose across the fixed cut used in the proof.

## Match and non-match readouts

Comparing two candidate ports gives different probabilities depending on whether the source is shared.

| Readout event | Unmatched | Matched |
| --- | --- | --- |
| Exchange has sign $`+1`$ | $`p_0=(d+1)/(2d)`$ | $`p_1=p_0+\theta(1-p_0)`$ |
| Common-basis outcomes coincide | $`q_0=1/d`$ | $`q_1=q_0+\theta(d-1)/(d(d+1))`$ |

For the first row, the symmetric subspace has dimension $`d(d+1)/2`$ and contains all the weight of the shared-draw state. For the second, the equal-outcome vectors $`|aa\rangle`$ are symmetric and span a $`d`$-dimensional subspace. The joint readout therefore has a margin of order $`\theta`$ even at large dimension. The local coincidence bit has an order-$`\theta/d`$ margin and an order-$`1/d`$ event probability.

## Continue reading

- [Receiver and implementation costs](receiver.md) explains how to examine overlapping possible links with one buffered batch.
- [Shot lower bounds](bounds.md) proves the joint and separable scaling and the stronger fixed-visibility port-local converse.
- [Interpretation](interpretation.md) identifies the resource behind the separation and the limits of the model.
