# Verification

Run the finite-instance checks from the repository root with Python 3. The script uses only the standard library.

```sh
python3 verification/check_pairing.py
```

The script represents small matrices as rational linear combinations of permutation operators. It checks that the source has trace one, confirms the exchange and common-basis collision probabilities for true and false links, and verifies the fixed-cut partial transpose identity entry by entry. The two quartet matchings and visibility values $`1/20`$, $`3/10`$, and $`1`$ are checked at local dimensions two and three.

For the [coherent receiver](../science/receiver.md), the script verifies a two-shot spectral threshold against a binomial tail and checks that all six noiseless link tests in the four-port example are projectors. With two shots, true links $`(1,2)`$ and $`(3,4)`$, and lexicographic edge order, the probability of a completely correct threshold record is exactly

```math
\frac{20537}{589824} \approx 0.0348188612.
```

The two-shot instance checks the sequential state-update calculation. The larger four-port guarantee comes from Gao's bound. Twenty-one noiseless shots give probability of failure at most $`16(3/4)^{21}\lt 0.05`$.
