# Related work

[BibTeX records](references.bib) for the scientific sources and the educational anchor.

## Shared source primitives and neighboring tasks

- Sentís, Monràs, Muñoz-Tapia, Calsamiglia and Bagan study unsupervised assignments of one batch to two unknown Haar prototypes. Their symmetry reduction yields an optimal classification measurement for that ensemble. Hidden source pairing has independently redrawn preparations and one persistent matching across shots. The target is the recurring source assignment of the ports. [Unsupervised Classification of Quantum Data](https://doi.org/10.1103/PhysRevX.9.041029)
- Chen, Doolittle, Larson, Saleem and Chitambar infer network topology with local measurements, using entropy, mutual information and covariance in source families that include GHZ states. The matched family here is separable and gives a finite-shot comparison against all local communication, including coherent processing within each port. [Inferring Quantum Network Topology Using Local Measurements](https://doi.org/10.1103/PRXQuantum.4.040347)
- Ananth, Gulati and Lin analyze same versus independent Haar states with the candidate locations given. Their Theorem 7.9 studies $`t`$ copies per side of one latent preparation and provides an LOCC indistinguishability bound. The present pair moment is inherited from the same basic primitive. Fresh latent draws in each shot let us study complete recovery of an initially unknown matching. [Cryptography in the Common Haar State Model](https://arxiv.org/abs/2407.07908)
- Anshu, Landau and Liu estimate the overlap of two fixed unknown states from copies held at separate locations. The candidate links here compare new latent draws each shot. Cross-time copies therefore provide a repeated test of the wiring rather than additional copies of any port's latent state. [Distributed Quantum Inner Product Estimation](https://arxiv.org/abs/2111.03273)
- Bouland, Giurgica-Tiron and Wright locate product cuts from repeated copies of a fixed pure state via a state hidden subgroup problem. Our snapshots are mixtures of product emissions and the matching identifies latent classical dependence. [The State Hidden Subgroup Problem and an Efficient Algorithm for Locating Unentanglement](https://arxiv.org/abs/2410.12706)

## Proof and implementation ingredients

- The normalized symmetric projector is the projective second moment of a Haar state. Exact projective 2-designs suffice. Zhu proves the stronger fact that the stabilizer orbit is a projective 3-design for multiqubit registers. [Multiqubit Clifford Groups Are Unitary 3-Designs](https://doi.org/10.1103/PhysRevA.96.062336)
- Gao's noncommutative union bound controls a sequence of projections on the same state through the sum of their initial failure probabilities. We use it for high-confidence thresholds of candidate exchange statistics. [Quantum Union Bounds for Sequential Projective Measurements](https://doi.org/10.1103/PhysRevA.92.052331)
- Werner-state data hiding develops distinguishability bounds under local and partial-transpose restrictions. Matthews and Winter analyze many copies of the two extremal bipartite Werner states. Akresh, Beckey and Leditzky give tight worst-case binary PPT hiding bounds for multipartite Werner states. The quartet proof here uses a common cut for a family of independent assignment bits, leading to a bound on exact recovery of the whole wiring. [Many-copy Werner discrimination](https://arxiv.org/abs/0710.4113), [multipartite Werner hiding](https://arxiv.org/abs/2609.40332)

## Paired quantum demonstrations

[Quantum Learning Readout](https://github.com/GoGoKo699/Quantum-Learning-Readout) uses the same two-register source family at the identity transformation. It supplies the correspondence and learns a continuous unitary in the fixed-dimension high-precision regime. [Quantum Learning Correspondence](https://github.com/GoGoKo699/Quantum-Learning-Correspondence) shuffles demonstrations across a whole batch and studies the consequences for learning that transformation. The current model holds the transform fixed, retains shot boundaries, and learns the persistent spatial correspondence under a finite shot budget.

[Quantum Clustering Early Readout](https://github.com/GoGoKo699/Quantum-Clustering-Early-Readout) uses one batch from fixed unknown prototypes and asks when a classical clustering record can be released while preserving optimal final accuracy. The overlapping link tests here concern a statistically recurring wiring, with a different measurement restriction and loss.
