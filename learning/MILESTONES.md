# Project understanding map

The first 12 milestones build the problem from a single register to an exact wiring-recovery task. The next 18 develop the exchange and common-basis receivers, then build the three lower bounds and their resource interpretation. Each milestone identifies a concept and its place in the proof. Use the [Watrous bridge](WATROUS_BRIDGE.md) for targeted readings and the [worked tutorial](TUTORIAL.md) to follow one experiment.

| Range | What comes together |
|---|---|
| [M01](#m01-one-specimen-at-one-port)–[M07](#m07-single-port-and-two-port-marginals) | A shared latent draw, a fixed hidden matching, and observable two-port marginals |
| [M08](#m08-effects-and-state-updates)–[M12](#m12-the-complete-recovery-problem) | Measurement, local processing restrictions, and whole-wiring recovery |
| [M13](#m13-two-outcomes-of-an-exchange-test)–[M19](#m19-shot-costs-and-circuit-costs) | Exchange and collision statistics, coherent reuse of shots, and circuit costs |
| [M20](#m20-a-global-reference-for-information)–[M25](#m25-exact-recovery-with-separable-effects) | Information lower bounds for unrestricted and specimen-separable receivers |
| [M26](#m26-a-common-cut-for-hidden-quartet-bits)–[M30](#m30-the-full-source-to-receiver-argument) | The stronger port-local converse, visibility scope, and the full comparison |

## Phase I · Background and preliminaries

### M01 One specimen at one port

**Central question.** What arrives at a single labeled output?

**Understanding target.** Treat one specimen as a density operator on a d-dimensional register, and distinguish its label from a classical description of its state.

**Prerequisites.** First milestone in the map.

**Conceptual connection.** The receiver sees where an emission arrived. Its state preparation record is hidden.

**Canonical sources.** [Scientific model](../science/model.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M02 Product preparations and latent randomness

**Central question.** How can two ports be correlated when each emitted shot is separable across ports?

**Understanding target.** Separate the product of two pure-state projectors conditioned on a shared draw from the mixture obtained after forgetting that draw.

**Prerequisites.** [M01](#m01-one-specimen-at-one-port).

**Conceptual connection.** Classical uncertainty about a shared preparation can create correlations without inter-port entanglement.

**Canonical sources.** [Scientific model](../science/model.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M03 The exchange operator

**Central question.** What changes when two port registers trade places?

**Understanding target.** Identify the exchange operator and its two eigenspaces. Explain why equal pure copies lie in the symmetric one.

**Prerequisites.** [M01](#m01-one-specimen-at-one-port), [M02](#m02-product-preparations-and-latent-randomness).

**Conceptual connection.** The eigenvalues give an operational statistic for whether two outputs could share a source.

**Canonical sources.** [Worked example](TUTORIAL.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M04 The isotropic pure state moment

**Central question.** Why does a random shared draw give a normalized projector?

**Understanding target.** Use unitary invariance and the two-copy moment to obtain the normalized symmetric projector. Identify the first moment of one output.

**Prerequisites.** [M02](#m02-product-preparations-and-latent-randomness), [M03](#m03-the-exchange-operator).

**Conceptual connection.** A projective 2-design reproduces both moments, so the analysis only needs these averaged operators.

**Canonical sources.** [Scientific model](../science/model.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M05 The visibility parameter

**Central question.** What is lost when a source emits two independent draws instead?

**Understanding target.** Express imperfect pair sharing as the convex mixture of the shared-state moment and the product of independent first moments.

**Prerequisites.** [M02](#m02-product-preparations-and-latent-randomness), [M04](#m04-the-isotropic-pure-state-moment).

**Conceptual connection.** Visibility determines the size of the statistical gap, while the local density operator stays fixed.

**Canonical sources.** [Scientific model](../science/model.md) · [Worked example](TUTORIAL.md).

### M06 A shot and its repetitions

**Central question.** Which parts of the data are the same between shots?

**Understanding target.** Distinguish the fixed matching from the freshly drawn states, and identify the tensor factors that index shot, port, and hidden source.

**Prerequisites.** [M02](#m02-product-preparations-and-latent-randomness), [M05](#m05-the-visibility-parameter).

**Conceptual connection.** The hidden wiring is the index of an independent and identically distributed sequence of quantum snapshots.

**Canonical sources.** [Scientific model](../science/model.md).

### M07 Single port and two port marginals

**Central question.** Where is information about the wiring stored?

**Understanding target.** Find the maximally mixed marginal at every individual port and tell which two-port marginals contain a shared-source term.

**Prerequisites.** [M04](#m04-the-isotropic-pure-state-moment), [M06](#m06-a-shot-and-its-repetitions).

**Conceptual connection.** The marginals make it possible to test a candidate edge without knowing what happens at the other ports.

**Canonical sources.** [Scientific model](../science/model.md) · [Worked example](TUTORIAL.md).

### M08 Effects and state updates

**Central question.** What does a measurement record describe when the state will be used again?

**Understanding target.** Separate a POVM effect from an instrument. Identify the state update given by a two-outcome projective measurement.

**Prerequisites.** [M01](#m01-one-specimen-at-one-port), [M03](#m03-the-exchange-operator).

**Conceptual connection.** Several candidate edges share input registers, so the correct record alone does not suffice to specify how to reuse the data.

**Canonical sources.** [Watrous bridge](WATROUS_BRIDGE.md) · [Receiver](../science/receiver.md).

### M09 Three receiver access classes

**Central question.** Where is a joint operation permitted?

**Understanding target.** Distinguish unrestricted processing, effects separable over individual specimens, and port-local processing with quantum memory across shots. Identify their different information and interaction resources.

**Prerequisites.** [M06](#m06-a-shot-and-its-repetitions), [M08](#m08-effects-and-state-updates).

**Conceptual connection.** The same data and target can support several valid baselines when their operations are specified.

**Canonical sources.** [Scientific model](../science/model.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M10 Partial transpose and a fixed cut

**Central question.** How can a tensor cut restrict allowable measurement effects?

**Understanding target.** Define a cut that assigns whole port streams to its sides. Explain why port-local classical communication yields effects whose partial transposes are positive on that cut.

**Prerequisites.** [M08](#m08-effects-and-state-updates), [M09](#m09-three-receiver-access-classes).

**Conceptual connection.** This turns a physically defined receiver restriction into an algebraic condition on its full transcript.

**Canonical sources.** [Watrous bridge](WATROUS_BRIDGE.md) · [Shot lower bounds](../science/bounds.md).

### M11 Statistical distinguishability

**Central question.** What does a difference in probabilities say about a finite decision budget?

**Understanding target.** Connect concentration to an achievable error bound, relative entropy to the information in a record, and binary trace distance or fidelity to the best two-hypothesis decision.

**Prerequisites.** [M05](#m05-the-visibility-parameter), [M08](#m08-effects-and-state-updates).

**Conceptual connection.** Upper bounds analyze a particular decision rule, while lower bounds limit every allowed record for the same task.

**Canonical sources.** [Watrous bridge](WATROUS_BRIDGE.md) · [Shot lower bounds](../science/bounds.md).

### M12 The complete recovery problem

**Central question.** What counts as a correct run of the full experiment?

**Understanding target.** State the unknown matching, the supplied port and shot labels, the visibility promise, and the requirement to recover every edge with failure at most the specified allowance.

**Prerequisites.** [M06](#m06-a-shot-and-its-repetitions), [M07](#m07-single-port-and-two-port-marginals), [M09](#m09-three-receiver-access-classes), [M10](#m10-partial-transpose-and-a-fixed-cut), [M11](#m11-statistical-distinguishability).

**Conceptual connection.** This combines the source and access assumptions into a single minimax question.

**Canonical sources.** [Scientific model](../science/model.md) · [Interpretation](../science/interpretation.md).

## Phase II · Narrative and innovation

### M13 Two outcomes of an exchange test

**Central question.** How does the exchange measurement reveal a candidate partner?

**Understanding target.** Compute the symmetric-outcome probabilities for a true edge and an unrelated pair, and identify their visibility-dependent gap.

**Prerequisites.** [M03](#m03-the-exchange-operator), [M05](#m05-the-visibility-parameter), [M07](#m07-single-port-and-two-port-marginals), [M12](#m12-the-complete-recovery-problem).

**Conceptual connection.** The size of the gap stays proportional to visibility as the register dimension increases.

**Canonical sources.** [Receiver](../science/receiver.md) · [Worked example](TUTORIAL.md).

### M14 The common basis comparison

**Central question.** What can a simple port-local receiver learn from each shot?

**Understanding target.** Measure each register in the same basis, then compute an equality indicator for each candidate link. Compare its null probability with the true-link probability.

**Prerequisites.** [M07](#m07-single-port-and-two-port-marginals), [M09](#m09-three-receiver-access-classes), [M12](#m12-the-complete-recovery-problem).

**Conceptual connection.** All candidate statistics are obtained from classical outputs. Their useful events become rare as the dimension increases.

**Canonical sources.** [Receiver](../science/receiver.md) · [Worked example](TUTORIAL.md).

### M15 Thresholds for one candidate edge

**Central question.** How many clean observations make a single edge decision reliable?

**Understanding target.** Explain the midpoint threshold and why exchange counts use a bounded-variable concentration bound while equality counts need their smaller variance to give the sharp rate.

**Prerequisites.** [M11](#m11-statistical-distinguishability), [M13](#m13-two-outcomes-of-an-exchange-test), [M14](#m14-the-common-basis-comparison).

**Conceptual connection.** The two forms of concentration connect the observed statistics to their different shot costs.

**Canonical sources.** [Receiver](../science/receiver.md).

### M16 Reversible counting

**Central question.** How do you read only the exchange threshold?

**Understanding target.** Compute the exchange signs coherently, compute the threshold into a separate flag, and reverse the sign and count computation before reading the flag.

**Prerequisites.** [M08](#m08-effects-and-state-updates), [M13](#m13-two-outcomes-of-an-exchange-test), [M15](#m15-thresholds-for-one-candidate-edge).

**Conceptual connection.** This realizes the two projective threshold effects while keeping coherence within each outcome subspace.

**Canonical sources.** [Receiver](../science/receiver.md).

### M17 One buffered batch for all edges

**Central question.** What controls disturbance between candidate tests that share a port?

**Understanding target.** Distinguish the error of each test on the input batch from its error after earlier projections. Use the quantum union bound to control the probability that the whole tested sequence is correct.

**Prerequisites.** [M08](#m08-effects-and-state-updates), [M15](#m15-thresholds-for-one-candidate-edge), [M16](#m16-reversible-counting).

**Conceptual connection.** The joint receiver reuses one batch for all edges even though its candidate effects can fail to commute.

**Canonical sources.** [Receiver](../science/receiver.md).

### M18 A complete four port run

**Central question.** How does the receiver turn six threshold decisions into two source links?

**Understanding target.** Walk through a fixed qubit matching. Compute the true and false exchange probabilities and turn the six candidate tests into a sufficient shot count for the desired failure allowance.

**Prerequisites.** [M13](#m13-two-outcomes-of-an-exchange-test), [M14](#m14-the-common-basis-comparison), [M17](#m17-one-buffered-batch-for-all-edges).

**Conceptual connection.** The toy experiment connects port labels, data registers, coherent computation, and the recovered edges.

**Canonical sources.** [Worked example](TUTORIAL.md) · [Verification](../verification/README.md).

### M19 Shot costs and circuit costs

**Central question.** Which physical resources does the receiver exchange for fewer snapshots?

**Understanding target.** Account for the specimens in a shot, the buffered registers, the pairwise exchange gates, and the classical comparison work. Distinguish shot count from elapsed time.

**Prerequisites.** [M09](#m09-three-receiver-access-classes), [M16](#m16-reversible-counting), [M17](#m17-one-buffered-batch-for-all-edges), [M18](#m18-a-complete-four-port-run).

**Conceptual connection.** The result compares matched data access. Gate connectivity and local memory determine different implementation costs.

**Canonical sources.** [Receiver](../science/receiver.md) · [Interpretation](../science/interpretation.md).

### M20 A global reference for information

**Central question.** How can we bound information without estimating every pair of matching states?

**Understanding target.** Compare every hidden-matching state to a fixed maximally mixed reference. Use the symmetric and antisymmetric sectors to obtain the divergence per true pair.

**Prerequisites.** [M07](#m07-single-port-and-two-port-marginals), [M11](#m11-statistical-distinguishability), [M12](#m12-the-complete-recovery-problem), [M13](#m13-two-outcomes-of-an-exchange-test).

**Conceptual connection.** The same reference works across the hypothesis family and avoids pair-by-pair comparison of its members.

**Canonical sources.** [Shot lower bounds](../science/bounds.md).

### M21 The cost of selecting a matching

**Central question.** Why does recovering every edge require logarithmically many shots even for a joint receiver?

**Understanding target.** Compare the entropy of a uniform hidden matching with the total reference divergence. Apply the Fano step to pass from an information budget to error at fixed confidence.

**Prerequisites.** [M12](#m12-the-complete-recovery-problem), [M20](#m20-a-global-reference-for-information).

**Conceptual connection.** Both the hypothesis entropy and each shot’s information scale with the number of links, leaving a logarithmic shot factor.

**Canonical sources.** [Shot lower bounds](../science/bounds.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M22 The cost of high confidence

**Central question.** Why does small target failure add a second logarithm?

**Understanding target.** Reduce to two matchings that differ within four ports. Use the overlap of the two resulting states and independence over shots to lower-bound binary error.

**Prerequisites.** [M11](#m11-statistical-distinguishability), [M18](#m18-a-complete-four-port-run), [M20](#m20-a-global-reference-for-information), [M21](#m21-the-cost-of-selecting-a-matching).

**Conceptual connection.** This reduction tracks the confidence cost even when the number of ports is fixed.

**Canonical sources.** [Shot lower bounds](../science/bounds.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M23 Product effects and likelihood ratios

**Central question.** What does an individual-specimen access restriction do to the full transcript?

**Understanding target.** Refine a separable measurement into product effects. Express its outcome likelihood against the mixed reference in terms of normalized local effect overlaps.

**Prerequisites.** [M08](#m08-effects-and-state-updates), [M09](#m09-three-receiver-access-classes), [M14](#m14-the-common-basis-comparison), [M20](#m20-a-global-reference-for-information).

**Conceptual connection.** This likelihood representation lets the converse cover more than the fixed-basis receiver.

**Canonical sources.** [Shot lower bounds](../science/bounds.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M24 The chord bound for separable readout

**Central question.** Why does an arbitrary refined record have limited divergence?

**Understanding target.** Bound a convex function of each local overlap by the chord through zero and one, then use POVM completeness to average the products on disjoint true pairs.

**Prerequisites.** [M11](#m11-statistical-distinguishability), [M23](#m23-product-effects-and-likelihood-ratios).

**Conceptual connection.** Common-basis effects attain the endpoint overlap values used by the bound, revealing the role of rare coincidences.

**Canonical sources.** [Shot lower bounds](../science/bounds.md).

### M25 Exact recovery with separable effects

**Central question.** How do the two directions of divergence enter the separable shot law?

**Understanding target.** Use forward divergence to bound the matching information and reverse divergence to constrain a high-confidence decision on a four-port subproblem.

**Prerequisites.** [M21](#m21-the-cost-of-selecting-a-matching), [M22](#m22-the-cost-of-high-confidence), [M23](#m23-product-effects-and-likelihood-ratios), [M24](#m24-the-chord-bound-for-separable-readout).

**Conceptual connection.** The information bound and the common-basis receiver together give the full visibility and dimension dependence in this access class.

**Canonical sources.** [Shot lower bounds](../science/bounds.md) · [Receiver](../science/receiver.md).

### M26 A common cut for hidden quartet bits

**Central question.** How can one cut cover many different candidate wirings?

**Understanding target.** Group ports into quartets, assign two ports per group to each side, and restrict each quartet to the two cross-cut perfect matchings.

**Prerequisites.** [M10](#m10-partial-transpose-and-a-fixed-cut), [M12](#m12-the-complete-recovery-problem), [M18](#m18-a-complete-four-port-run).

**Conceptual connection.** A fixed cut lets one transform all candidate states and one receiver’s effects consistently.

**Canonical sources.** [Shot lower bounds](../science/bounds.md).

### M27 The partial transpose mixture

**Central question.** Why does temporal memory at individual ports still leave difficult shots?

**Understanding target.** Transpose the effects and states across the fixed cut. Interpret the transformed state as a mixture with a small weight on a maximally entangled component.

**Prerequisites.** [M05](#m05-the-visibility-parameter), [M10](#m10-partial-transpose-and-a-fixed-cut), [M26](#m26-a-common-cut-for-hidden-quartet-bits).

**Conceptual connection.** The mixture is a proof device that preserves the original measurement probabilities despite representing the states differently.

**Canonical sources.** [Shot lower bounds](../science/bounds.md) · [Watrous bridge](WATROUS_BRIDGE.md).

### M28 Unrevealed wiring bits

**Central question.** How can independent quartets force an exact recovery cost?

**Understanding target.** Give the hypothetical receiver mixture flags and the true bit of each flagged group. Bound its probability of identifying the remaining bits, then use the bound to constrain the original receiver.

**Prerequisites.** [M22](#m22-the-cost-of-high-confidence), [M26](#m26-a-common-cut-for-hidden-quartet-bits), [M27](#m27-the-partial-transpose-mixture).

**Conceptual connection.** Each entirely unflagged group contributes a hidden bit, which explains how the logarithm in the full-port local law arises.

**Canonical sources.** [Shot lower bounds](../science/bounds.md).

### M29 Scope of the weak visibility bounds

**Central question.** Which dimension and visibility claims follow for each receiver?

**Understanding target.** State the matching visibility-dependent rates for unrestricted and specimen-separable measurements and the remaining interval for temporal port-local processing.

**Prerequisites.** [M19](#m19-shot-costs-and-circuit-costs), [M25](#m25-exact-recovery-with-separable-effects), [M28](#m28-unrevealed-wiring-bits).

**Conceptual connection.** This keeps the unresolved dependence at weak signal from changing the fixed-positive-visibility result.

**Canonical sources.** [Scientific model](../science/model.md) · [Interpretation](../science/interpretation.md) · [Shot lower bounds](../science/bounds.md).

### M30 The full source to receiver argument

**Central question.** Why does this experiment give a quantum shot advantage with separable data?

**Understanding target.** Reconstruct the chain from shared draws to exchange statistics, coherent reuse, and the local converse. State exactly what is learned and which purchased resources yield the advantage.

**Prerequisites.** [M12](#m12-the-complete-recovery-problem), [M19](#m19-shot-costs-and-circuit-costs), [M21](#m21-the-cost-of-selecting-a-matching), [M22](#m22-the-cost-of-high-confidence), [M25](#m25-exact-recovery-with-separable-effects), [M28](#m28-unrevealed-wiring-bits), [M29](#m29-scope-of-the-weak-visibility-bounds).

**Conceptual connection.** The output is recurrent source wiring. The comparison joins a concrete receiver and measurements on the same physical input model.

**Canonical sources.** [Scientific model](../science/model.md) · [Interpretation](../science/interpretation.md) · [Worked example](TUTORIAL.md) · [Verification](../verification/README.md).
