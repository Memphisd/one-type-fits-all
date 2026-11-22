# Comparisons with earlier algorithms

The paper compares its decoders and filters with earlier algorithms and with filters of [HG26]. These are not
representation trees as in the paper: a single nearest-neighbour join, Stern's algorithm over F_q, the center count of
Hirose [Hir16], filters with three sets of positions [HG26], trees whose joins below the top also filter syndrome
coordinates [BM18], and the decoders of [BBPSWW23]. The scripts of this folder compute the paper's numbers for them.
Each prints one line per number: where it is in the paper, the value rounded as the paper rounds it (exponents up,
differences down, values of earlier work to nearest), and the unrounded value. Comparing with the paper is left to
the reader.

Install jointtrees as described in the README one folder up. `common.py` holds what the scripts share: rounding,
entropies, the error weight of decoding over F_q and the center count of Hirose.

```sh
python3 single_nn_join.py              # Table 4, under a second
python3 stern.py                       # Table 7, columns Stern and Hirose, under a second
python3 three_sets.py                  # Appendix D, comparison with [HG26], under a second
python3 both_may.py                    # Section 7, join architectures and footnote, under a second
python3 single_nn_join.py --optimize   # Table 4 from 20 random starts per cell, about 30 seconds (numpy, scipy)
python3 stern.py --optimize            # Table 7 as the worst case over the grid of rates, about a minute (numpy, scipy)
python3 restricted_published.py REST_DEC   # Table 9, column "published [BBPSWW23]", 30 seconds (see below)
```

| script | numbers | model |
|---|---|---|
| `single_nn_join.py` | Table 4 (Section 7), all 15 cells: one nearest-neighbour join over F_q without a filter, with Hirose's center count, and with the filter of [neighbour join] | the cost of the filtered join with the filter exponents of the paper, and Hirose's center count [Hir16, Theorem 1] |
| `stern.py` | Table 7 (Appendix E), the 27 cells of the columns Stern (half and full distance) and Hirose (half distance) | Stern's algorithm over F_q with an exact join and with Hirose's nearest-neighbour join, each the worst case over a grid of rates of step 0.002 |
| `three_sets.py` | Appendix D, comparison with [HG26]: 0.2691 (digits -1..2, depth 5) and 0.2605 (digits -2..2, depth 6, two parts), and the gain over two sets | the exponents of [HG26, Prop. 3] in the paper's cost of the filtered join, on trees evaluated by jointtrees. For two sets the script reproduces the library's filter exponents |
| `both_may.py` | Section 7, the paragraph on join architectures and its footnote on [BM18]: 2 searches with free blocks, 24 with a forced block, and the 7 decoder trees they start from | the decoder of the paper with blocks of syndrome coordinates filtered at the joins below the top, checked against jointtrees on the 7 decoder trees |
| `restricted_published.py` | Table 9 (Appendix G), the 6 cells of the column "published [BBPSWW23]" (q = 157, R = 0.5) | the authors' code, github.com/sebastianbitzer/rest-dec, unchanged, run with fixed seeds. [BBPSWW23] shows these exponents only as curves (Figs. 2 and 3). REST_DEC is a checkout of that repository |

## Data

| file | content |
|---|---|
| `data/single_nn_join.json` | per row of Table 4: q, L, gamma, Hirose's center size u and share h0 of the digit 0, the center size u and price z0 of the filter of [neighbour join] |
| `data/stern.json` | per cell: q, distance, grid of rates, worst rate and the parameters there |
| `data/three_sets/*.json` | per tree: a witness of jointtrees whose two-set filters filter nothing, and the filters with three sets per join and part |
| `data/both_may.json` | per end point: the cell, the decoder's witness it started from, the parameters of jointtrees plus the blocks |
| `data/restricted_published.json` | per cell: z, omega, the number of representation levels of the decoder of [BBPSWW23] and the seed of numpy of the lowest valid run |
