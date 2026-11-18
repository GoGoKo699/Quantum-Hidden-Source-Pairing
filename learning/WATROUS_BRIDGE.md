# From Watrous to hidden source pairing

The educational anchor is **John Watrous, *The Theory of Quantum Information***, Cambridge University Press, 2018. The section numbers refer to the author’s January 2018 prepublication manuscript. The author provides the manuscript and separately identifies the April 2018 publication date. [Author’s page and manuscript chapters](https://cs.uwaterloo.ca/~watrous/TQI/).

Start with the [worked four-port experiment](TUTORIAL.md). Read the following passages as their objects appear. The [milestone map](MILESTONES.md) connects them to the complete research account.

## Targeted readings

| Where to read | What to carry into the project |
|---|---|
| [§§2.1.2–2.1.3, chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Pure and mixed states, classical ensembles, and partial trace. Trace out all ports except one to recover its local state. |
| [§§2.3.1–2.3.2, chapter 2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf) | Treat a complete classical record as a POVM. Keep the state update when successive tests reuse the batch. |
| [§7.1.1 and §7.2.1, chapter 7](https://cs.uwaterloo.ca/~watrous/TQI/TQI.7.pdf) | Construct the symmetric projector from permutations. Lemma 7.24, p. 416, gives the Haar pure-state moment that becomes the true-link density operator. |
| [§§6.1.1–6.1.3 and §6.2.3, chapter 6](https://cs.uwaterloo.ca/~watrous/TQI/TQI.6.pdf) | Distinguish a separable source from an LOCC measurement. Use positivity after cutting the port registers into two groups. |
| [§3.1.1 and §3.2, chapter 3](https://cs.uwaterloo.ca/~watrous/TQI/TQI.3.pdf) | Theorem 3.4 connects trace distance to binary decision error. Theorem 3.33 bounds trace distance using fidelity, which multiplies over independent shots. |
| [§§5.1.1–5.1.2 and §5.2.3, chapter 5](https://cs.uwaterloo.ca/~watrous/TQI/TQI.5.pdf) | Use classical and quantum relative entropy. Theorem 5.35 bounds how much divergence a measurement can retain. The chapter’s exercises also point to Fano’s inequality, which gives the decoding step. |

## Translate the notation

| Watrous | Here |
|---|---|
| $`\mathcal X`$ and $`\mathcal Y`$ | Port register spaces, or all spaces assigned to the two sides of a lower-bound cut. |
| $`uu^*`$ | $`\lvert\psi\rangle\langle\psi\rvert`$, the projector describing a latent pure state. |
| $`W_\pi`$ | For a two-register transposition, the exchange operator $`F`$. |
| $`\Pi_{\mathrm{sym}}`$ | For two registers, $`P_+=(I+F)/2`$. |
| $`\mu(a)`$ | A measurement effect for outcome $`a`$, including a possible complete transcript. |
| $`T`$ as a transpose map | Superscript $`\Gamma`$ for partial transpose on the chosen side. The unadorned $`T`$ in this project counts shots. |
| Fidelity $`F(\rho,\sigma)`$ | Root fidelity $`\lVert\sqrt{\rho}\sqrt{\sigma}\rVert_1`$. Its square appears in a binary confidence bound. |
| Relative entropy with base-two logs | The project uses natural logarithms. Multiplying Watrous’s relative entropy by $`\ln 2`$ converts bits to nats. |

## The steps from textbook objects to the learning task

**From a moment to a hidden network.** Apply Lemma 7.24 with two copies of a single draw. The second moment is $`P_+/\mathrm{Tr}(P_+)`$. The first moment is $`I/d`$, so two independent draws average to $`I/d^2`$. On the unknown true links the source interpolates between these two states. Taking the tensor product over links and repeating independently over shots produces a finite family of data states indexed by matchings. The receiver learns the index of the data state. [Model](../science/model.md).

**From a measurement to reused evidence.** Section 2.3 explains the difference between an effect and a physical instrument. Measuring every individual exchange sign and keeping only its count generally changes the state more than performing a projective measurement of the threshold. The receiver computes and uncomputes the signs so that only the threshold is measured. Gao’s quantum union bound then controls errors across the full sequence of candidate checks. [Receiver](../science/receiver.md).

**From a marginal state to a receiver lower bound.** Two proofs use distinct entries from chapter 6. If the receiver’s effects factor after refinement over individual specimens, convexity and POVM completeness bound how much of a pair’s likelihood it can retain. If it may keep all shots coherently within each port, the proof uses positivity under partial transpose across a fixed cut. Exchange turns into $`d\lvert\Phi\rangle\langle\Phi\rvert`$ after transposing one end, where $`\lvert\Phi\rangle=d^{-1/2}\sum_i\lvert i,i\rangle`$. The resulting mixture hides each quartet’s wiring whenever all its rare terms are absent. Partial transpose is used as a proof identity on states and effects. [Shot lower bounds](../science/bounds.md).

**From one probability gap to whole-wiring recovery.** The project adds concentration for the measured statistics, an information budget over all possible wirings, and two-hypothesis comparisons for a stringent failure allowance. This keeps the number of ports, register dimension, visibility, and target confidence in the same shot law. [Shot lower bounds](../science/bounds.md) · [Interpretation](../science/interpretation.md).
