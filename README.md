# Quantum Hidden Source Pairing

**Which two ports are fed by the same source?** Each shot supplies one quantum register at each labeled port. Connected ports sometimes receive the same random preparation. Preparations are redrawn independently on the next shot, and each port viewed alone is maximally mixed. A joint receiver learns the entire wiring from separable snapshots.

For $`m`$ ports, local dimension $`d=2^n`$, known visibility $`\theta\gt 0`$ and target failure probability $`\delta\le 1/4`$, the shot bounds are:

| Measurement access | Shots for exact recovery |
| --- | --- |
| Joint readout across ports and shots | $`\Theta(\theta^{-2}\log(m/\delta))`$ |
| Separable measurements over individual port-shot specimens | $`\Theta(d\,\theta^{-2}\log(m/\delta))`$ |
| Port-local processing with temporal quantum memory and classical communication | $`\Theta(d\log(m/\delta))`$ at fixed positive $`\theta`$ |

Thus at fixed visibility, the shot penalty for port-local processing is exponential in the number of qubits per port. The joint receiver buffers complete shots, tests each candidate link with a reversible threshold of SWAP signs, and reads only the threshold bit for that link. Its gate count and storage are explicit. It is an advantage in shots and emitted specimens. Wall-clock costs depend on the available memory, gates and routing.

## Read the result

| Question | Where to start |
| --- | --- |
| Which states are supplied and what counts as learning the wiring? | [Snapshot model](science/model.md) |
| How can the receiver test links that share a port? | [Threshold receiver and resource accounting](science/receiver.md) |
| Why can local quantum memory fail to close the gap? | [Exact-recovery lower bounds](science/bounds.md) |
| What can a source or receiver engineer infer from it? | [Interpretation](science/interpretation.md) |
| How does this relate to quantum clustering and network inference? | [Related work](references/RELATED_WORK.md) |

For a worked four-port example, start with the [tutorial](learning/TUTORIAL.md). The [learning guide](learning/README.md) connects John Watrous's *The Theory of Quantum Information* to the result through the [source bridge](learning/WATROUS_BRIDGE.md) and [30 milestones](learning/MILESTONES.md).

Run the deterministic finite checks from this directory:

```bash
python3 verification/check_pairing.py
```

[Verification notes](verification/README.md) describe the checks and their scope.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).
