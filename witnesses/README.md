# Witnesses of the paper's numbers

Each file is a witness in the format of the library jointtrees (its docs/GUIDE.md, "Witness files"): the problem, the
tree, the memory bound, the claimed exponents, the free parameters under the paper's names, the values that follow
from them, and a note that says what the tree is. The table below gives, for every number of the paper that a tree
of this library computes, the file that backs it. `recompute/numbers.csv` holds the same list with the quantity and
the rounding, and `recompute/check_numbers.py` recomputes every number from its file.

```sh
python3 -m jointtrees verify witnesses                # all of them (install as in the README one folder up)
python3 -m jointtrees evaluate witnesses/subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json   # one tree
```

| folder | files | content |
|---|---|---|
| `decoding/` | 68 | decoding over F_q (Section 7) |
| `lee/` | 6 | the Lee metric (Appendix H) |
| `lwe/` | 29 | LWE with small keys (Section 6) |
| `restricted/` | 19 | restricted errors (Appendix G) |
| `subsetsum/` | 74 | subset sum: digit sets, depths, partitioning, the time-memory trade-off, the tree of Theorem 1 |
| `ternary/` | 7 | ternary decoding with large weight (Appendix F) |

The paper rounds exponents up and differences of exponents down.

Numbers without a file here:
- comparisons with earlier algorithms and with filters of [HG26], computed by the scripts in `comparisons/`,
- counts and closed-form values.

File names follow one scheme: the problem, the instance, the depth d, then the tree.

| part of the name | meaning |
|---|---|
| `digits-2to2` | the digits the lists use, here -2, ..., 2 |
| `filter`, `nofilter` | filters with prices on the joins 1 to d, or on none |
| `exact`, `mixed`, `nn` | the top join of a decoder: exact, exact and by distance, or by distance only |
| `parts2` | the positions are partitioned into two parts |
| `M0.25` | memory at most 2^(0.25 n), with the 7-dissection at join 0 and repetitions |
| `dissection` | without a memory bound, with the 7-dissection at join 0 |
| `full`, `half`, `R0.442` | the weight at the Gilbert-Varshamov distance or half of it, and the rate |
| `ternary0.5`, `binomial2`, `uniform2` | the LWE key: ternary of weight 0.5, centered binomial, uniform on -2, ..., 2 |
| `z4`, `W0.4` | restricted errors: the size of E and the weight |
| `joins-SFFFFF` | the joins 1 to d from the bottom: S a split join, F a filtered join, R a join without filter |
| `reoptimized` | a later run on the same tree that reached a slightly lower time |

## Which file backs which number

Places are the tables, figures, sections and appendices of the paper in its version of November 2026. Rows follow the
order of the paper.

| where in the paper | printed | witness |
|---|---|---|
| Abstract | 0.2620 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Section 1 | 0.2719 | `subsetsum/subsetsum_digits-2to2_d6_filter.json`<br>`subsetsum/subsetsum_digits-2to2_d5_filter.json` |
| Section 1 | 0.2724 | `subsetsum/subsetsum_digits-1to2_d5_filter.json` |
| Section 1, against [EMS24] and [GM23], low end | 0.0388 | `lwe/lwe_ternary0.3_digits-3to3_d10_filter_parts2.json` |
| Section 1, against [EMS24] and [GM23], high end | 0.0826 | `lwe/lwe_uniform2_digits-5to5_d14_filter_parts2.json` |
| Table 1 (Section 1), row 1 no filters | 0.2827 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_dissection.json` |
| Table 1 (Section 1), row 1 with filters | 0.2719 | `subsetsum/subsetsum_digits-2to2_d6_filter.json`<br>`subsetsum/subsetsum_digits-2to2_d5_filter.json` |
| Table 1 (Section 1), ternary, weight n/2 no filters | 0.3193 | `lwe/lwe_ternary0.5_digits-2to2_d5_nofilter.json` |
| Table 1 (Section 1), ternary, weight n/2 with filters | 0.2935 | `lwe/lwe_ternary0.5_digits-3to3_d17_filter.json` |
| Table 1 (Section 1), Kyber768/1024 no filters | 0.3397 | `lwe/lwe_binomial2_digits-3to3_d7_nofilter.json` |
| Table 1 (Section 1), Kyber768/1024 with filters | 0.2997 | `lwe/lwe_binomial2_digits-5to5_d17_filter.json` |
| Table 1 (Section 1), Kyber512 no filters | 0.3458 | `lwe/lwe_binomial3_digits-4to4_d8_nofilter.json` |
| Table 1 (Section 1), Kyber512 with filters | 0.3084 | `lwe/lwe_binomial3_digits-5to5_d13_filter.json` |
| Table 1 (Section 1), Dilithium no filters | 0.3620 | `lwe/lwe_uniform2_digits-3to3_d8_nofilter.json` |
| Table 1 (Section 1), Dilithium with filters | 0.3107 | `lwe/lwe_uniform2_digits-5to5_d14_filter.json` |
| Table 1 (Section 1), ternary, hardest no filters | 0.2304 | `ternary/ternary_hardest_d3_joins-SRR_exact.json` |
| Table 1 (Section 1), ternary, hardest with filters | 0.2179 | `ternary/ternary_hardest_d6_joins-SFFFFF_nn.json` |
| Table 1 (Section 1), restricted no filters | 0.2239 | `restricted/restricted_z2_W0.8_d5_exact.json` |
| Table 1 (Section 1), restricted with filters | 0.1962 | `restricted/restricted_z2_W0.8_d8_mixed_filter.json` |
| Table 1 (Section 1), Lee, q=47 no filters | 0.4058 | `lee/lee_q47_full_R0.48_d6_exact.json` |
| Table 1 (Section 1), restricted errors, partitioning | 0.1931 | `restricted/restricted_z2_W0.8_d9_mixed_filter_parts2.json` |
| Table 1 (Section 1), ternary decoding, partitioning | 0.2148 | `ternary/ternary_hardest_d7_joins-SFFFFFF_nn_parts2.json` |
| Table 1 (Section 1), subset sum, partitioning | 0.2620 | `subsetsum/subsetsum_digits-3to3_d6_filter_parts2.json` |
| Table 1 (Section 1), LWE ternary n/2, partitioning | 0.2684 | `lwe/lwe_ternary0.5_digits-3to3_d16_filter_parts2.json` |
| Table 1 (Section 1), LWE Kyber768/1024, partitioning | 0.2761 | `lwe/lwe_binomial2_digits-5to5_d17_filter_parts2.json` |
| Table 1 (Section 1), LWE Kyber512, partitioning | 0.3006 | `lwe/lwe_binomial3_digits-5to5_d13_filter_parts2.json` |
| Table 1 (Section 1), LWE Dilithium, partitioning | 0.2954 | `lwe/lwe_uniform2_digits-5to5_d14_filter_parts2.json` |
| Table 1 (Section 1), decoding over F_4, no filters | 0.1995 | `decoding/decoding_q4_full_R0.432_d2_exact.json` |
| Table 1 (Section 1), decoding over F_4, with filters and partitioning | 0.1972 | `decoding/decoding_q4_full_R0.43_d3_mixed.json` |
| Table 1 (Section 1), Lee metric, with filters | 0.3580 | `lee/lee_q47_full_R0.55_d7_filter.json` |
| Table 1 (Section 1), Lee metric, partitioning | 0.3580 | `lee/lee_q47_full_R0.55_d7_filter.json` |
| Figure 1 (Section 1) blue M=0.05 (faded) | 0.7366 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.05.json` |
| Figure 1 (Section 1) blue M=0.06 (faded) | 0.6985 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.06.json` |
| Figure 1 (Section 1) blue M=0.07 (faded) | 0.6687 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.07.json` |
| Figure 1 (Section 1) blue M=0.08 (faded) | 0.6400 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.08.json` |
| Figure 1 (Section 1) blue M=0.09 (faded) | 0.6121 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.09.json` |
| Figure 1 (Section 1) blue M=0.1 (label 3) | 0.5847 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.1.json` |
| Figure 1 (Section 1) blue M=0.1, depth label | 3 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.1.json` |
| Figure 1 (Section 1) blue M=0.125 (label 3) | 0.5180 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.125.json` |
| Figure 1 (Section 1) blue M=0.125, depth label | 3 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.125.json` |
| Figure 1 (Section 1) blue M=0.15 (label 3) | 0.4527 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.15.json` |
| Figure 1 (Section 1) blue M=0.15, depth label | 3 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.15.json` |
| Figure 1 (Section 1) blue M=0.175 (label 10) | 0.3814 | `subsetsum/subsetsum_digits-2to2_d10_nofilter_M0.175.json` |
| Figure 1 (Section 1) blue M=0.175, depth label | 10 | `subsetsum/subsetsum_digits-2to2_d10_nofilter_M0.175.json` |
| Figure 1 (Section 1) blue M=0.1875 (label 8) | 0.3539 | `subsetsum/subsetsum_digits-2to2_d8_nofilter_M0.1875.json` |
| Figure 1 (Section 1) blue M=0.1875, depth label | 8 | `subsetsum/subsetsum_digits-2to2_d8_nofilter_M0.1875.json` |
| Figure 1 (Section 1) blue M=0.2 (label 5) | 0.3407 | `subsetsum/subsetsum_digits-2to2_d5_nofilter_M0.2.json` |
| Figure 1 (Section 1) blue M=0.2, depth label | 5 | `subsetsum/subsetsum_digits-2to2_d5_nofilter_M0.2.json` |
| Figure 1 (Section 1) blue M=0.2125 (label 4) | 0.3282 | `subsetsum/subsetsum_digits-2to2_d4_nofilter_M0.2125.json` |
| Figure 1 (Section 1) blue M=0.2125, depth label | 4 | `subsetsum/subsetsum_digits-2to2_d4_nofilter_M0.2125.json` |
| Figure 1 (Section 1) blue M=0.225 (label 4) | 0.3166 | `subsetsum/subsetsum_digits-2to2_d4_nofilter_M0.225.json` |
| Figure 1 (Section 1) blue M=0.225, depth label | 4 | `subsetsum/subsetsum_digits-2to2_d4_nofilter_M0.225.json` |
| Figure 1 (Section 1) blue M=0.25 (label 4) | 0.2969 | `subsetsum/subsetsum_digits-2to2_d4_nofilter_M0.25.json` |
| Figure 1 (Section 1) blue M=0.25, depth label | 4 | `subsetsum/subsetsum_digits-2to2_d4_nofilter_M0.25.json` |
| Figure 1 (Section 1) blue M=0.275 (label 3) | 0.2848 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.275.json` |
| Figure 1 (Section 1) blue M=0.275, depth label | 3 | `subsetsum/subsetsum_digits-2to2_d3_nofilter_M0.275.json` |
| Figure 1 (Section 1) red M=0.05 (faded) | 0.7303 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.05.json` |
| Figure 1 (Section 1) red M=0.06 (faded) | 0.6925 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.06.json` |
| Figure 1 (Section 1) red M=0.07 (faded) | 0.6619 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.07.json` |
| Figure 1 (Section 1) red M=0.08 (faded) | 0.6324 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.08.json` |
| Figure 1 (Section 1) red M=0.09 (label 3) | 0.6038 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.09.json` |
| Figure 1 (Section 1) red M=0.09, depth label | 3 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.09.json` |
| Figure 1 (Section 1) red M=0.1 (label 3) | 0.5757 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.1.json` |
| Figure 1 (Section 1) red M=0.1, depth label | 3 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.1.json` |
| Figure 1 (Section 1) red M=0.125 (label 3) | 0.5069 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.125.json` |
| Figure 1 (Section 1) red M=0.125, depth label | 3 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.125.json` |
| Figure 1 (Section 1) red M=0.15 (label 3) | 0.4390 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.15.json` |
| Figure 1 (Section 1) red M=0.15, depth label | 3 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.15.json` |
| Figure 1 (Section 1) red M=0.175 (label 11) | 0.3649 | `subsetsum/subsetsum_digits-2to2_d11_filter_M0.175.json` |
| Figure 1 (Section 1) red M=0.175, depth label | 11 | `subsetsum/subsetsum_digits-2to2_d11_filter_M0.175.json` |
| Figure 1 (Section 1) red M=0.1875 (label 17) | 0.3201 | `subsetsum/subsetsum_digits-2to2_d17_filter_M0.1875.json` |
| Figure 1 (Section 1) red M=0.1875, depth label | 17 | `subsetsum/subsetsum_digits-2to2_d17_filter_M0.1875.json` |
| Figure 1 (Section 1) red M=0.2 (label 12) | 0.2845 | `subsetsum/subsetsum_digits-2to2_d12_filter_M0.2.json` |
| Figure 1 (Section 1) red M=0.2, depth label | 12 | `subsetsum/subsetsum_digits-2to2_d12_filter_M0.2.json` |
| Figure 1 (Section 1) red M=0.2125 (label 8) | 0.2801 | `subsetsum/subsetsum_digits-2to2_d8_filter_M0.2125.json` |
| Figure 1 (Section 1) red M=0.2125, depth label | 8 | `subsetsum/subsetsum_digits-2to2_d8_filter_M0.2125.json` |
| Figure 1 (Section 1) red M=0.225 (label 6) | 0.2765 | `subsetsum/subsetsum_digits-2to2_d6_filter_M0.225.json` |
| Figure 1 (Section 1) red M=0.225, depth label | 6 | `subsetsum/subsetsum_digits-2to2_d6_filter_M0.225.json` |
| Figure 1 (Section 1) red M=0.25 (label 5) | 0.2724 | `subsetsum/subsetsum_digits-2to2_d5_filter_M0.25.json` |
| Figure 1 (Section 1) red M=0.25, depth label | 5 | `subsetsum/subsetsum_digits-2to2_d5_filter_M0.25.json` |
| Figure 1 (Section 1) red end point M=0.267 (label 5) | 0.2719 | `subsetsum/subsetsum_digits-2to2_d5_filter_M0.267.json` |
| Figure 1 (Section 1) red end point M=0.267, depth label | 5 | `subsetsum/subsetsum_digits-2to2_d5_filter_M0.267.json` |
| Figure 1 (Section 1) orange M=0.05 (faded) | 0.7303 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.05.json` |
| Figure 1 (Section 1) orange M=0.06 (faded) | 0.6925 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.06.json` |
| Figure 1 (Section 1) orange M=0.07 (faded) | 0.6619 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.07.json` |
| Figure 1 (Section 1) orange M=0.08 (faded) | 0.6324 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.08.json` |
| Figure 1 (Section 1) red start point, M | 0.0879 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.0879.json` |
| Figure 1 (Section 1) red start point, time | 0.6097 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.0879.json` |
| Figure 1 (Section 1) orange start point, M | 0.0878 | `subsetsum/subsetsum_digits-2to2_d3_filter_parts2_M0.0878.json` |
| Figure 1 (Section 1) orange start point, time | 0.6097 | `subsetsum/subsetsum_digits-2to2_d3_filter_parts2_M0.0878.json` |
| Figure 1 (Section 1) orange M=0.09 (label 3) | 0.6034 | `subsetsum/subsetsum_digits-2to2_d3_filter_parts2_M0.09.json` |
| Figure 1 (Section 1) orange M=0.09, depth label | 3 | `subsetsum/subsetsum_digits-2to2_d3_filter_parts2_M0.09.json` |
| Figure 1 (Section 1) orange M=0.1 (label 3) | 0.5743 | `subsetsum/subsetsum_digits-2to2_d3_filter_parts2_M0.1.json` |
| Figure 1 (Section 1) orange M=0.1, depth label | 3 | `subsetsum/subsetsum_digits-2to2_d3_filter_parts2_M0.1.json` |
| Figure 1 (Section 1) orange M=0.125 (label 7) | 0.4896 | `subsetsum/subsetsum_digits-2to2_d7_filter_parts2_M0.125.json` |
| Figure 1 (Section 1) orange M=0.125, depth label | 7 | `subsetsum/subsetsum_digits-2to2_d7_filter_parts2_M0.125.json` |
| Figure 1 (Section 1) orange M=0.15 (label 12) | 0.3870 | `subsetsum/subsetsum_digits-2to2_d12_filter_parts2_M0.15.json` |
| Figure 1 (Section 1) orange M=0.15, depth label | 12 | `subsetsum/subsetsum_digits-2to2_d12_filter_parts2_M0.15.json` |
| Figure 1 (Section 1) orange M=0.175 (label 10) | 0.3065 | `subsetsum/subsetsum_digits-2to2_d10_filter_parts2_M0.175.json` |
| Figure 1 (Section 1) orange M=0.175, depth label | 10 | `subsetsum/subsetsum_digits-2to2_d10_filter_parts2_M0.175.json` |
| Figure 1 (Section 1) orange M=0.1875 (label 9) | 0.2778 | `subsetsum/subsetsum_digits-2to2_d9_filter_parts2_M0.1875.json` |
| Figure 1 (Section 1) orange M=0.1875, depth label | 9 | `subsetsum/subsetsum_digits-2to2_d9_filter_parts2_M0.1875.json` |
| Figure 1 (Section 1) orange M=0.2 (label 8) | 0.2640 | `subsetsum/subsetsum_digits-2to2_d8_filter_parts2_M0.2.json` |
| Figure 1 (Section 1) orange M=0.2, depth label | 8 | `subsetsum/subsetsum_digits-2to2_d8_filter_parts2_M0.2.json` |
| Figure 1 (Section 1) orange M=0.2125 (label 7) | 0.2621 | `subsetsum/subsetsum_digits-2to2_d7_filter_parts2_M0.2125.json` |
| Figure 1 (Section 1) orange M=0.2125, depth label | 7 | `subsetsum/subsetsum_digits-2to2_d7_filter_parts2_M0.2125.json` |
| Figure 4 (Section 4), theta of the pair (2, -1) | 0.997 | `subsetsum/subsetsum_digits-1to2_d5_filter.json` |
| Figure 4 (Section 4), theta of the pair (1, -1) | 0.940 | `subsetsum/subsetsum_digits-1to2_d5_filter.json` |
| Figure 4 (Section 4), theta of the pair (1, 0) | 0.754 | `subsetsum/subsetsum_digits-1to2_d5_filter.json` |
| Figure 4 (Section 4), theta of the pair (0, 0) | 0.500 | `subsetsum/subsetsum_digits-1to2_d5_filter.json` |
| Figure 4 (Section 4), theta of the pair (0, 1) | 0.246 | `subsetsum/subsetsum_digits-1to2_d5_filter.json` |
| Figure 4 (Section 4), theta of the pair (-1, 1) | 0.060 | `subsetsum/subsetsum_digits-1to2_d5_filter.json` |
| Figure 4 (Section 4), theta of the pair (-1, 2) | 0.003 | `subsetsum/subsetsum_digits-1to2_d5_filter.json` |
| Section 5 | 0.2829 | `subsetsum/subsetsum_digits-1to2_d3_nofilter_dissection.json` |
| Section 5 | 0.2835 | `subsetsum/subsetsum_digits-1to2_d4_nofilter_dissection.json` |
| Section 5 | 0.2719 | `subsetsum/subsetsum_digits-2to2_d6_filter.json` |
| Section 5 | 0.2621 | `subsetsum/subsetsum_digits-2to2_d6_filter_parts2.json` |
| Section 5 | 0.2620 | `subsetsum/subsetsum_digits-3to3_d6_filter_parts2.json` |
| Section 5 | below 10^{-5} | `subsetsum/subsetsum_digits-4to4_d6_filter_parts2.json`<br>`subsetsum/subsetsum_digits-3to3_d6_filter_parts2_reoptimized.json` |
| Section 5 | (depth increased until no change) | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2.json` |
| Section 5 | M >= 0.088 | `subsetsum/subsetsum_digits-1to2_d3_filter_M0.088.json` |
| Section 5 | M >= 0.088 | `subsetsum/subsetsum_digits-2to2_d3_filter_M0.088.json` |
| Section 5 | 0.3407 | `subsetsum/subsetsum_digits-2to2_d5_nofilter_M0.2.json` |
| Section 5 | 0.0561 | `subsetsum/subsetsum_digits-2to2_d5_nofilter_M0.2.json`<br>`subsetsum/subsetsum_digits-2to2_d12_filter_M0.2.json` |
| Section 5, digits {-1,0,1,2} d=3 | 0.2791 | `subsetsum/subsetsum_digits-1to2_d3_filter.json` |
| Section 5, digits {-1,0,1,2} d=4 | 0.2726 | `subsetsum/subsetsum_digits-1to2_d4_filter.json` |
| Section 5, digits {-1,0,1,2} d=5 | 0.2724 | `subsetsum/subsetsum_digits-1to2_d5_filter_reoptimized.json` |
| Section 5, memory at depth 6 | 0.2560 | `subsetsum/subsetsum_digits-3to3_d6_filter_parts2.json` |
| Section 5, M = 0.2, [EZ23] minus ours with filters | 0.0712 | `subsetsum/subsetsum_digits-2to2_d12_filter_M0.2.json` |
| Section 5, M = 0.2, [EZ23] minus ours with partitioning | 0.0917 | `subsetsum/subsetsum_digits-2to2_d8_filter_parts2_M0.2.json` |
| Section 5, M = 0.2, gain of partitioning | 0.0205 | `subsetsum/subsetsum_digits-2to2_d12_filter_M0.2.json`<br>`subsetsum/subsetsum_digits-2to2_d8_filter_parts2_M0.2.json` |
| Table 2 (Section 5) {0,1} d=3, no filters | 0.3372 | `subsetsum/subsetsum_digits0to1_d3_nofilter_M0.35.json` |
| Table 2 (Section 5) {0,1} d=3, with filters | 0.3270 | `subsetsum/subsetsum_digits0to1_d3_filter.json` |
| Table 2 (Section 5) {0,1} d=3, partitioning | 0.3270 | `subsetsum/subsetsum_digits0to1_d3_filter.json` |
| Table 2 (Section 5) {-1,0,1} d=3, no filters | 0.2892 | `subsetsum/subsetsum_digits-1to1_d3_nofilter_dissection.json` |
| Table 2 (Section 5) {-1,0,1} d=3, with filters | 0.2844 | `subsetsum/subsetsum_digits-1to1_d3_filter.json` |
| Table 2 (Section 5) {-1,0,1} d=3, partitioning | 0.2843 | `subsetsum/subsetsum_digits-1to1_d3_filter_parts2.json` |
| Table 2 (Section 5) {-1,0,1} d=4, no filters | 0.2896 | `subsetsum/subsetsum_digits-1to1_d4_nofilter_dissection.json` |
| Table 2 (Section 5) {-1,0,1} d=4, with filters | 0.2800 | `subsetsum/subsetsum_digits-1to1_d4_filter.json` |
| Table 2 (Section 5) {-1,0,1} d=4, partitioning | 0.2798 | `subsetsum/subsetsum_digits-1to1_d4_filter_parts2.json` |
| Table 2 (Section 5) {-1,0,1,2} d=3, no filters | 0.2829 | `subsetsum/subsetsum_digits-1to2_d3_nofilter_dissection.json` |
| Table 2 (Section 5) {-1,0,1,2} d=3, with filters | 0.2791 | `subsetsum/subsetsum_digits-1to2_d3_filter.json` |
| Table 2 (Section 5) {-1,0,1,2} d=3, partitioning | 0.2791 | `subsetsum/subsetsum_digits-1to2_d3_filter_parts2.json` |
| Table 2 (Section 5) {-1,0,1,2} d=4, no filters | 0.2835 | `subsetsum/subsetsum_digits-1to2_d4_nofilter_dissection.json` |
| Table 2 (Section 5) {-1,0,1,2} d=4, with filters | 0.2726 | `subsetsum/subsetsum_digits-1to2_d4_filter.json` |
| Table 2 (Section 5) {-1,0,1,2} d=4, partitioning | 0.2707 | `subsetsum/subsetsum_digits-1to2_d4_filter_parts2.json` |
| Table 2 (Section 5) {-1,0,1,2} d=5, no filters | 0.2835 | `subsetsum/subsetsum_digits-1to2_d5_nofilter_dissection.json` |
| Table 2 (Section 5) {-1,0,1,2} d=5, with filters | 0.2724 | `subsetsum/subsetsum_digits-1to2_d5_filter_reoptimized.json` |
| Table 2 (Section 5) {-1,0,1,2} d=5, partitioning | 0.2668 | `subsetsum/subsetsum_digits-1to2_d5_filter_parts2.json` |
| Table 2 (Section 5) {-2..2} d=6, no filters | 0.2833 | `subsetsum/subsetsum_digits-2to2_d6_nofilter.json` |
| Table 2 (Section 5) {-2..2} d=6, with filters | 0.2719 | `subsetsum/subsetsum_digits-2to2_d6_filter.json` |
| Table 2 (Section 5) {-2..2} d=6, partitioning | 0.2621 | `subsetsum/subsetsum_digits-2to2_d6_filter_parts2.json` |
| Table 2 (Section 5) {-3..3} d=6, no filters | 0.2833 | `subsetsum/subsetsum_digits-3to3_d6_nofilter.json` |
| Table 2 (Section 5) {-3..3} d=6, with filters | 0.2719 | `subsetsum/subsetsum_digits-3to3_d6_filter.json` |
| Table 2 (Section 5) {-3..3} d=6, partitioning | 0.2620 | `subsetsum/subsetsum_digits-3to3_d6_filter_parts2.json` |
| Theorem 1 (Section 5) | 0.2620 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Theorem 1 (Section 5) | 0.2120 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Proof of Theorem 1 (Section 5) | 0.2120 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 3 (Section 6) omega=0.3, no filters (d=5) | 0.2884 | `lwe/lwe_ternary0.3_digits-2to2_d5_nofilter.json` |
| Table 3 (Section 6) omega=0.3, no filters, depth | 5 | `lwe/lwe_ternary0.3_digits-2to2_d5_nofilter.json` |
| Table 3 (Section 6) omega=0.3, with filters (d=5) | 0.2787 | `lwe/lwe_ternary0.3_digits-3to3_d5_filter.json` |
| Table 3 (Section 6) omega=0.3, with filters, depth | 5 | `lwe/lwe_ternary0.3_digits-3to3_d5_filter.json` |
| Table 3 (Section 6) omega=0.3, partitioning (d=10) | 0.2505 | `lwe/lwe_ternary0.3_digits-3to3_d10_filter_parts2.json` |
| Table 3 (Section 6) omega=0.3, partitioning, depth | 10 | `lwe/lwe_ternary0.3_digits-3to3_d10_filter_parts2.json` |
| Table 3 (Section 6) omega=0.375, no filters (d=5) | 0.3042 | `lwe/lwe_ternary0.375_digits-2to2_d5_nofilter.json` |
| Table 3 (Section 6) omega=0.375, no filters, depth | 5 | `lwe/lwe_ternary0.375_digits-2to2_d5_nofilter.json` |
| Table 3 (Section 6) omega=0.375, with filters (d=7) | 0.2889 | `lwe/lwe_ternary0.375_digits-3to3_d7_filter.json` |
| Table 3 (Section 6) omega=0.375, with filters, depth | 7 | `lwe/lwe_ternary0.375_digits-3to3_d7_filter.json` |
| Table 3 (Section 6) omega=0.375, partitioning (d=14) | 0.2596 | `lwe/lwe_ternary0.375_digits-3to3_d14_filter_parts2.json` |
| Table 3 (Section 6) omega=0.375, partitioning, depth | 14 | `lwe/lwe_ternary0.375_digits-3to3_d14_filter_parts2.json` |
| Table 3 (Section 6) omega=0.441, no filters (d=5) | 0.3139 | `lwe/lwe_ternary0.441_digits-2to2_d5_nofilter.json` |
| Table 3 (Section 6) omega=0.441, no filters, depth | 5 | `lwe/lwe_ternary0.441_digits-2to2_d5_nofilter.json` |
| Table 3 (Section 6) omega=0.441, with filters (d=11) | 0.2924 | `lwe/lwe_ternary0.441_digits-3to3_d11_filter.json` |
| Table 3 (Section 6) omega=0.441, with filters, depth | 11 | `lwe/lwe_ternary0.441_digits-3to3_d11_filter.json` |
| Table 3 (Section 6) omega=0.441, partitioning (d=15) | 0.2647 | `lwe/lwe_ternary0.441_digits-3to3_d15_filter_parts2.json` |
| Table 3 (Section 6) omega=0.441, partitioning, depth | 15 | `lwe/lwe_ternary0.441_digits-3to3_d15_filter_parts2.json` |
| Table 3 (Section 6) omega=0.5, no filters (d=5) | 0.3193 | `lwe/lwe_ternary0.5_digits-2to2_d5_nofilter.json` |
| Table 3 (Section 6) omega=0.5, no filters, depth | 5 | `lwe/lwe_ternary0.5_digits-2to2_d5_nofilter.json` |
| Table 3 (Section 6) omega=0.5, with filters (d=17) | 0.2935 | `lwe/lwe_ternary0.5_digits-3to3_d17_filter.json` |
| Table 3 (Section 6) omega=0.5, with filters, depth | 17 | `lwe/lwe_ternary0.5_digits-3to3_d17_filter.json` |
| Table 3 (Section 6) omega=0.5, partitioning (d=16) | 0.2684 | `lwe/lwe_ternary0.5_digits-3to3_d16_filter_parts2.json` |
| Table 3 (Section 6) omega=0.5, partitioning, depth | 16 | `lwe/lwe_ternary0.5_digits-3to3_d16_filter_parts2.json` |
| Table 3 (Section 6) omega=0.62, no filters (d=5) | 0.3287 | `lwe/lwe_ternary0.62_digits-2to2_d5_nofilter.json` |
| Table 3 (Section 6) omega=0.62, no filters, depth | 5 | `lwe/lwe_ternary0.62_digits-2to2_d5_nofilter.json` |
| Table 3 (Section 6) omega=0.62, with filters (d=20) | 0.2949 | `lwe/lwe_ternary0.62_digits-3to3_d20_filter.json` |
| Table 3 (Section 6) omega=0.62, with filters, depth | 20 | `lwe/lwe_ternary0.62_digits-3to3_d20_filter.json` |
| Table 3 (Section 6) omega=0.62, partitioning (d=20) | 0.2741 | `lwe/lwe_ternary0.62_digits-3to3_d20_filter_parts2.json` |
| Table 3 (Section 6) omega=0.62, partitioning, depth | 20 | `lwe/lwe_ternary0.62_digits-3to3_d20_filter_parts2.json` |
| Table 3 (Section 6) omega=0.667, no filters (d=5) | 0.3320 | `lwe/lwe_ternary0.667_digits-2to2_d5_nofilter.json` |
| Table 3 (Section 6) omega=0.667, no filters, depth | 5 | `lwe/lwe_ternary0.667_digits-2to2_d5_nofilter.json` |
| Table 3 (Section 6) omega=0.667, with filters (d=20) | 0.2955 | `lwe/lwe_ternary0.667_digits-3to3_d20_filter.json` |
| Table 3 (Section 6) omega=0.667, with filters, depth | 20 | `lwe/lwe_ternary0.667_digits-3to3_d20_filter.json` |
| Table 3 (Section 6) omega=0.667, partitioning (d=20) | 0.2759 | `lwe/lwe_ternary0.667_digits-3to3_d20_filter_parts2.json` |
| Table 3 (Section 6) omega=0.667, partitioning, depth | 20 | `lwe/lwe_ternary0.667_digits-3to3_d20_filter_parts2.json` |
| Table 3 (Section 6) B(2), no filters (d=7) | 0.3397 | `lwe/lwe_binomial2_digits-3to3_d7_nofilter.json` |
| Table 3 (Section 6) B(2), no filters, depth | 7 | `lwe/lwe_binomial2_digits-3to3_d7_nofilter.json` |
| Table 3 (Section 6) B(2), with filters (d=17) | 0.2997 | `lwe/lwe_binomial2_digits-5to5_d17_filter.json` |
| Table 3 (Section 6) B(2), with filters, depth | 17 | `lwe/lwe_binomial2_digits-5to5_d17_filter.json` |
| Table 3 (Section 6) B(2), partitioning (d=17) | 0.2761 | `lwe/lwe_binomial2_digits-5to5_d17_filter_parts2.json` |
| Table 3 (Section 6) B(2), partitioning, depth | 17 | `lwe/lwe_binomial2_digits-5to5_d17_filter_parts2.json` |
| Table 3 (Section 6) B(3), no filters (d=8) | 0.3458 | `lwe/lwe_binomial3_digits-4to4_d8_nofilter.json` |
| Table 3 (Section 6) B(3), no filters, depth | 8 | `lwe/lwe_binomial3_digits-4to4_d8_nofilter.json` |
| Table 3 (Section 6) B(3), with filters (d=13) | 0.3084 | `lwe/lwe_binomial3_digits-5to5_d13_filter.json` |
| Table 3 (Section 6) B(3), with filters, depth | 13 | `lwe/lwe_binomial3_digits-5to5_d13_filter.json` |
| Table 3 (Section 6) B(3), partitioning (d=13) | 0.3006 | `lwe/lwe_binomial3_digits-5to5_d13_filter_parts2.json` |
| Table 3 (Section 6) B(3), partitioning, depth | 13 | `lwe/lwe_binomial3_digits-5to5_d13_filter_parts2.json` |
| Table 3 (Section 6) U(2), no filters (d=8) | 0.3620 | `lwe/lwe_uniform2_digits-3to3_d8_nofilter.json` |
| Table 3 (Section 6) U(2), no filters, depth | 8 | `lwe/lwe_uniform2_digits-3to3_d8_nofilter.json` |
| Table 3 (Section 6) U(2), with filters (d=14) | 0.3107 | `lwe/lwe_uniform2_digits-5to5_d14_filter.json` |
| Table 3 (Section 6) U(2), with filters, depth | 14 | `lwe/lwe_uniform2_digits-5to5_d14_filter.json` |
| Table 3 (Section 6) U(2), partitioning (d=14) | 0.2954 | `lwe/lwe_uniform2_digits-5to5_d14_filter_parts2.json` |
| Table 3 (Section 6) U(2), partitioning, depth | 14 | `lwe/lwe_uniform2_digits-5to5_d14_filter_parts2.json` |
| Section 7, beats Meurer's BJMM for all q up to 27 at half distance (no file yet for q = 9, 17, 25) | claim | `decoding/decoding_q13_half_R0.496_d1_exact.json`<br>`decoding/decoding_q13_half_R0.496_d2_exact.json`<br>`decoding/decoding_q13_half_R0.496_d2_mixed.json`<br>`decoding/decoding_q13_half_R0.498_d1_mixed.json`<br>`decoding/decoding_q19_half_R0.504_d1_exact.json`<br>`decoding/decoding_q19_half_R0.504_d1_mixed.json`<br>`decoding/decoding_q19_half_R0.504_d2_exact.json`<br>`decoding/decoding_q19_half_R0.504_d2_mixed.json`<br>`decoding/decoding_q23_half_R0.506_d1_exact.json`<br>`decoding/decoding_q23_half_R0.506_d1_mixed.json`<br>`decoding/decoding_q23_half_R0.506_d2_exact.json`<br>`decoding/decoding_q23_half_R0.506_d2_mixed.json`<br>`decoding/decoding_q32_half_R0.512_d1_exact.json`<br>`decoding/decoding_q32_half_R0.512_d1_mixed.json`<br>`decoding/decoding_q32_half_R0.512_d2_exact.json`<br>`decoding/decoding_q32_half_R0.512_d2_mixed.json` |
| Table 5 (Section 7) q=2 half, Alg. isd (d=2) | 0.0473 | `decoding/decoding_q2_half_R0.463_d2_mixed.json` |
| Table 5 (Section 7) q=2 full, Alg. isd (d=3) | 0.0953 | `decoding/decoding_q2_full_R0.422_d3_mixed.json` |
| Table 5 (Section 7) q=3 half, BJMM (gray) | 0.0751 | `decoding/decoding_q3_half_R0.466_d2_exact.json` |
| Table 5 (Section 7) q=3 half, Alg. isd (d=2) | 0.0730 | `decoding/decoding_q3_half_R0.47_d2_mixed.json` |
| Table 5 (Section 7) q=3 full, BJMM (gray, d=2) | 0.1598 | `decoding/decoding_q3_full_R0.43_d2_exact.json` |
| Table 5 (Section 7) q=3 full, Alg. isd (d=3) | 0.1561 | `decoding/decoding_q3_full_R0.428_d3_mixed.json` |
| Table 5 (Section 7) q=4 half, BJMM (gray) | 0.0920 | `decoding/decoding_q4_half_R0.472_d2_exact.json` |
| Table 5 (Section 7) q=4 half, Alg. isd (d=2) | 0.0900 | `decoding/decoding_q4_half_R0.474_d2_mixed.json` |
| Table 5 (Section 7) q=4 full, BJMM (green, d=2) | 0.1995 | `decoding/decoding_q4_full_R0.432_d2_exact.json` |
| Table 5 (Section 7) q=4 full, Alg. isd (d=3) | 0.1972 | `decoding/decoding_q4_full_R0.43_d3_mixed.json` |
| Table 5 (Section 7) q=5 half, BJMM (gray) | 0.1042 | `decoding/decoding_q5_half_R0.477_d2_exact.json` |
| Table 5 (Section 7) q=5 half, Alg. isd (d=2) | 0.1025 | `decoding/decoding_q5_half_R0.479_d2_mixed.json` |
| Table 5 (Section 7) q=5 full, BJMM (gray, d=2) | 0.2294 | `decoding/decoding_q5_full_R0.434_d2_exact.json` |
| Table 5 (Section 7) q=5 full, Alg. isd (d=2) | 0.2278 | `decoding/decoding_q5_full_R0.432_d2_mixed.json` |
| Table 5 (Section 7) q=7 half, BJMM (gray) | 0.1212 | `decoding/decoding_q7_half_R0.484_d2_exact.json` |
| Table 5 (Section 7) q=7 half, Alg. isd (d=2) | 0.1201 | `decoding/decoding_q7_half_R0.486_d2_mixed.json` |
| Table 5 (Section 7) q=7 full, BJMM (gray, d=2) | 0.2724 | `decoding/decoding_q7_full_R0.438_d2_exact.json` |
| Table 5 (Section 7) q=7 full, Alg. isd (d=2) | 0.2718 | `decoding/decoding_q7_full_R0.436_d2_mixed.json` |
| Table 5 (Section 7) q=8 half, BJMM (gray) | 0.1275 | `decoding/decoding_q8_half_R0.488_d2_exact.json` |
| Table 5 (Section 7) q=8 half, Alg. isd (d=2) | 0.1266 | `decoding/decoding_q8_half_R0.488_d2_mixed.json` |
| Table 5 (Section 7) q=8 full, BJMM (green, d=2) | 0.2888 | `decoding/decoding_q8_full_R0.438_d2_exact.json` |
| Table 5 (Section 7) q=8 full, Alg. isd (d=2) | 0.2884 | `decoding/decoding_q8_full_R0.438_d2_mixed.json` |
| Table 5 (Section 7) q=11 half, BJMM (gray) | 0.1416 | `decoding/decoding_q11_half_R0.494_d2_exact.json` |
| Table 5 (Section 7) q=11 half, Alg. isd (d=2) | 0.1410 | `decoding/decoding_q11_half_R0.494_d2_mixed.json` |
| Table 5 (Section 7) q=11 full, BJMM (gray, d=2) | 0.3262 | `decoding/decoding_q11_full_R0.442_d2_exact.json` |
| Table 5 (Section 7) q=11 full, Alg. isd (d=2) | 0.3261 | `decoding/decoding_q11_full_R0.442_d2_mixed.json` |
| Table 5 (Section 7) q=16 half, BJMM (gray) | 0.1564 | `decoding/decoding_q16_half_R0.5_d2_exact.json` |
| Table 5 (Section 7) q=16 half, Alg. isd (d=2) | 0.1560 | `decoding/decoding_q16_half_R0.5_d2_mixed.json` |
| Table 5 (Section 7) q=16 full, BJMM (green, d=2) | 0.3667 | `decoding/decoding_q16_full_R0.446_d2_exact.json` |
| Table 5 (Section 7) q=16 full, Alg. isd (d=2) | 0.3667 | `decoding/decoding_q16_full_R0.446_d2_mixed.json` |
| Table 5 (Section 7) q=27 half, BJMM (gray) | 0.1741 | `decoding/decoding_q27_half_R0.508_d2_exact.json` |
| Table 5 (Section 7) q=27 half, Alg. isd (d=2) | 0.1740 | `decoding/decoding_q27_half_R0.508_d2_mixed.json` |
| Table 5 (Section 7) q=27 full, BJMM (gray, d=1) | 0.4164 | `decoding/decoding_q27_full_R0.452_d1_exact.json` |
| Table 5 (Section 7) q=27 full, Alg. isd (d=1) | 0.4164 | `decoding/decoding_q27_full_R0.452_d1_mixed.json` |
| Appendix D (comparison with HG26), digits {-1,0,1,2} d=3 | 0.2791 | `subsetsum/subsetsum_digits-1to2_d3_filter.json` |
| Appendix D (comparison with HG26), digits {-1,0,1,2} d=4 | 0.2726 | `subsetsum/subsetsum_digits-1to2_d4_filter.json` |
| Appendix D (comparison with HG26), digits {-1,0,1,2} d=5 | 0.2724 | `subsetsum/subsetsum_digits-1to2_d5_filter_reoptimized.json` |
| Appendix D (comparison with HG26), from | 0.2724 | `subsetsum/subsetsum_digits-1to2_d5_filter_reoptimized.json` |
| Appendix D (comparison with HG26), gain over [HG26] with filters, low end | 0.0128 | `lwe/lwe_ternary0.3_digits-3to3_d5_filter.json` |
| Appendix D (comparison with HG26), gain over [HG26] with filters, high end | 0.0888 | `lwe/lwe_ternary0.667_digits-3to3_d20_filter.json` |
| Appendix D (comparison with HG26), gain over [HG26] with partitioning, low end | 0.0410 | `lwe/lwe_ternary0.3_digits-3to3_d10_filter_parts2.json` |
| Appendix D (comparison with HG26), gain over [HG26] with partitioning, high end | 0.1084 | `lwe/lwe_ternary0.667_digits-3to3_d20_filter_parts2.json` |
| Appendix D (comparison with HG26), digits {-1,0,1}, no filters | 0.3511 | `lwe/lwe_ternary0.5_digits-1to1_d4_nofilter.json` |
| Appendix D (comparison with HG26), digits {-1,0,1}, with filters | 0.3341 | `lwe/lwe_ternary0.5_digits-1to1_d5_filter.json` |
| Table 6 (Appendix D) omega=0.3, no filters | 0.2884 | `lwe/lwe_ternary0.3_digits-2to2_d5_nofilter.json` |
| Table 6 (Appendix D) omega=0.3, with filters | 0.2787 | `lwe/lwe_ternary0.3_digits-3to3_d5_filter.json` |
| Table 6 (Appendix D) omega=0.3, partitioning | 0.2505 | `lwe/lwe_ternary0.3_digits-3to3_d10_filter_parts2.json` |
| Table 6 (Appendix D) omega=0.375, no filters | 0.3042 | `lwe/lwe_ternary0.375_digits-2to2_d5_nofilter.json` |
| Table 6 (Appendix D) omega=0.375, with filters | 0.2889 | `lwe/lwe_ternary0.375_digits-3to3_d7_filter.json` |
| Table 6 (Appendix D) omega=0.375, partitioning | 0.2596 | `lwe/lwe_ternary0.375_digits-3to3_d14_filter_parts2.json` |
| Table 6 (Appendix D) omega=0.441, no filters | 0.3139 | `lwe/lwe_ternary0.441_digits-2to2_d5_nofilter.json` |
| Table 6 (Appendix D) omega=0.441, with filters | 0.2924 | `lwe/lwe_ternary0.441_digits-3to3_d11_filter.json` |
| Table 6 (Appendix D) omega=0.441, partitioning | 0.2647 | `lwe/lwe_ternary0.441_digits-3to3_d15_filter_parts2.json` |
| Table 6 (Appendix D) omega=0.5, no filters | 0.3193 | `lwe/lwe_ternary0.5_digits-2to2_d5_nofilter.json` |
| Table 6 (Appendix D) omega=0.5, with filters | 0.2935 | `lwe/lwe_ternary0.5_digits-3to3_d17_filter.json` |
| Table 6 (Appendix D) omega=0.5, partitioning | 0.2684 | `lwe/lwe_ternary0.5_digits-3to3_d16_filter_parts2.json` |
| Table 6 (Appendix D) omega=0.62, no filters | 0.3287 | `lwe/lwe_ternary0.62_digits-2to2_d5_nofilter.json` |
| Table 6 (Appendix D) omega=0.62, with filters | 0.2949 | `lwe/lwe_ternary0.62_digits-3to3_d20_filter.json` |
| Table 6 (Appendix D) omega=0.62, partitioning | 0.2741 | `lwe/lwe_ternary0.62_digits-3to3_d20_filter_parts2.json` |
| Table 6 (Appendix D) omega=0.667, no filters | 0.3320 | `lwe/lwe_ternary0.667_digits-2to2_d5_nofilter.json` |
| Table 6 (Appendix D) omega=0.667, with filters | 0.2955 | `lwe/lwe_ternary0.667_digits-3to3_d20_filter.json` |
| Table 6 (Appendix D) omega=0.667, partitioning | 0.2759 | `lwe/lwe_ternary0.667_digits-3to3_d20_filter_parts2.json` |
| Table 7 (Appendix E) q=2 half, Stern-NN | 0.0550 | `decoding/decoding_q2_half_R0.466_d0_nn.json` |
| Table 7 (Appendix E) q=2 full, Stern-NN | 0.1138 | `decoding/decoding_q2_full_R0.446_d0_nn.json` |
| Table 7 (Appendix E) q=3 half, Stern-NN | 0.0823 | `decoding/decoding_q3_half_R0.474_d0_nn.json` |
| Table 7 (Appendix E) q=3 full, Stern-NN | 0.1761 | `decoding/decoding_q3_full_R0.448_d0_nn.json` |
| Table 7 (Appendix E) q=4 half, Stern-NN | 0.0995 | `decoding/decoding_q4_half_R0.48_d0_nn.json` |
| Table 7 (Appendix E) q=4 full, Stern-NN | 0.2171 | `decoding/decoding_q4_full_R0.45_d0_nn.json` |
| Table 7 (Appendix E) q=5 half, Stern-NN | 0.1116 | `decoding/decoding_q5_half_R0.484_d0_nn.json` |
| Table 7 (Appendix E) q=5 full, Stern-NN | 0.2471 | `decoding/decoding_q5_full_R0.452_d0_nn.json` |
| Table 7 (Appendix E) q=7 half, Stern-NN | 0.1282 | `decoding/decoding_q7_half_R0.49_d0_nn.json` |
| Table 7 (Appendix E) q=7 full, Stern-NN | 0.2891 | `decoding/decoding_q7_full_R0.452_d0_nn.json` |
| Table 7 (Appendix E) q=8 half, Stern-NN | 0.1343 | `decoding/decoding_q8_half_R0.494_d0_nn.json` |
| Table 7 (Appendix E) q=8 full, Stern-NN | 0.3048 | `decoding/decoding_q8_full_R0.454_d0_nn.json` |
| Table 7 (Appendix E) q=11 half, Stern-NN | 0.1476 | `decoding/decoding_q11_half_R0.498_d0_nn.json` |
| Table 7 (Appendix E) q=11 full, Stern-NN | 0.3399 | `decoding/decoding_q11_full_R0.454_d0_nn.json` |
| Table 7 (Appendix E) q=16 half, Stern-NN | 0.1614 | `decoding/decoding_q16_half_R0.504_d0_nn.json` |
| Table 7 (Appendix E) q=16 full, Stern-NN | 0.3774 | `decoding/decoding_q16_full_R0.457_d0_nn.json` |
| Table 7 (Appendix E) q=27 half, Stern-NN | 0.1779 | `decoding/decoding_q27_half_R0.512_d0_nn.json` |
| Table 7 (Appendix E) q=27 full, Stern-NN | 0.4238 | `decoding/decoding_q27_full_R0.457_d0_nn.json` |
| Appendix F, hardest instance, no filters | 0.2304 | `ternary/ternary_hardest_d3_joins-SRR_exact.json` |
| Appendix F, hardest instance, with filters | 0.2179 | `ternary/ternary_hardest_d6_joins-SFFFFF_nn.json` |
| Appendix F, Wave R=0.5, with filters | 0.0142 | `ternary/ternary_wave_R0.5_d6_joins-SFFSSS_nn.json` |
| Appendix F, Wave R=0.676, with filters | 0.0167 | `ternary/ternary_wave_R0.676_d6_joins-SFFSSS_nn.json` |
| Table 8 (Appendix F) hardest, no filters | 0.2304 | `ternary/ternary_hardest_d3_joins-SRR_exact.json` |
| Table 8 (Appendix F) hardest, with filters | 0.2179 | `ternary/ternary_hardest_d6_joins-SFFFFF_nn.json` |
| Table 8 (Appendix F) hardest, two parts | 0.2148 | `ternary/ternary_hardest_d7_joins-SFFFFFF_nn_parts2.json` |
| Table 8 (Appendix F) Wave R=0.5, no filters | 0.0148 | `ternary/ternary_wave_R0.5_d6_joins-SRRSSS_exact.json` |
| Table 8 (Appendix F) Wave R=0.5, with filters | 0.0142 | `ternary/ternary_wave_R0.5_d6_joins-SFFSSS_nn.json` |
| Table 8 (Appendix F) Wave R=0.676, no filters | 0.0176 | `ternary/ternary_wave_R0.676_d6_joins-SRRSSS_exact.json` |
| Table 8 (Appendix F) Wave R=0.676, with filters | 0.0167 | `ternary/ternary_wave_R0.676_d6_joins-SFFSSS_nn.json` |
| Appendix G | within 10^{-3} | `restricted/restricted_z2_W0.4_d3_exact.json` |
| Appendix G | within 10^{-3} | `restricted/restricted_z2_W0.6_d3_exact.json` |
| Appendix G | within 10^{-3} | `restricted/restricted_z2_W0.8_d3_exact.json` |
| Table 9 (Appendix G) z=2 w=0.2, no filters (d=2) | 0.1334 | `restricted/restricted_z2_W0.2_d2_exact.json` |
| Table 9 (Appendix G) z=2 w=0.2, no filters, depth | 2 | `restricted/restricted_z2_W0.2_d2_exact.json` |
| Table 9 (Appendix G) z=2 w=0.2, with filters (d=3) | 0.1294 | `restricted/restricted_z2_W0.2_d3_mixed_filter.json` |
| Table 9 (Appendix G) z=2 w=0.2, with filters, depth | 3 | `restricted/restricted_z2_W0.2_d3_mixed_filter.json` |
| Table 9 (Appendix G) z=2 w=0.4, no filters (d=4) | 0.1869 | `restricted/restricted_z2_W0.4_d4_exact.json` |
| Table 9 (Appendix G) z=2 w=0.4, no filters, depth | 4 | `restricted/restricted_z2_W0.4_d4_exact.json` |
| Table 9 (Appendix G) z=2 w=0.4, with filters (d=5) | 0.1725 | `restricted/restricted_z2_W0.4_d5_mixed_filter.json` |
| Table 9 (Appendix G) z=2 w=0.4, with filters, depth | 5 | `restricted/restricted_z2_W0.4_d5_mixed_filter.json` |
| Table 9 (Appendix G) z=2 w=0.6, no filters (d=5) | 0.2099 | `restricted/restricted_z2_W0.6_d5_exact.json` |
| Table 9 (Appendix G) z=2 w=0.6, no filters, depth | 5 | `restricted/restricted_z2_W0.6_d5_exact.json` |
| Table 9 (Appendix G) z=2 w=0.6, with filters (d=11) | 0.1849 | `restricted/restricted_z2_W0.6_d11_mixed_filter.json` |
| Table 9 (Appendix G) z=2 w=0.6, with filters, depth | 11 | `restricted/restricted_z2_W0.6_d11_mixed_filter.json` |
| Table 9 (Appendix G) z=2 w=0.8, no filters (d=5) | 0.2239 | `restricted/restricted_z2_W0.8_d5_exact.json` |
| Table 9 (Appendix G) z=2 w=0.8, no filters, depth | 5 | `restricted/restricted_z2_W0.8_d5_exact.json` |
| Table 9 (Appendix G) z=2 w=0.8, with filters (d=8) | 0.1962 | `restricted/restricted_z2_W0.8_d8_mixed_filter.json` |
| Table 9 (Appendix G) z=2 w=0.8, with filters, depth | 8 | `restricted/restricted_z2_W0.8_d8_mixed_filter.json` |
| Table 9 (Appendix G) z=4 w=0.4, no filters (d=2) | 0.3038 | `restricted/restricted_z4_W0.4_d2_exact.json` |
| Table 9 (Appendix G) z=4 w=0.4, no filters, depth | 2 | `restricted/restricted_z4_W0.4_d2_exact.json` |
| Table 9 (Appendix G) z=4 w=0.4, with filters (d=3) | 0.2849 | `restricted/restricted_z4_W0.4_d3_mixed_filter.json` |
| Table 9 (Appendix G) z=4 w=0.4, with filters, depth | 3 | `restricted/restricted_z4_W0.4_d3_mixed_filter.json` |
| Table 9 (Appendix G) z=4 w=0.6, no filters (d=3) | 0.3990 | `restricted/restricted_z4_W0.6_d3_exact.json` |
| Table 9 (Appendix G) z=4 w=0.6, no filters, depth | 3 | `restricted/restricted_z4_W0.6_d3_exact.json` |
| Table 9 (Appendix G) z=4 w=0.6, with filters (d=3) | 0.3723 | `restricted/restricted_z4_W0.6_d3_mixed_filter.json` |
| Table 9 (Appendix G) z=4 w=0.6, with filters, depth | 3 | `restricted/restricted_z4_W0.6_d3_mixed_filter.json` |
| Table 9 (Appendix G) z=2 w=0.2, two parts | 0.1294 | `restricted/restricted_z2_W0.2_d3_mixed_filter.json` |
| Table 9 (Appendix G) z=2 w=0.2, two parts, d | 3 | `restricted/restricted_z2_W0.2_d3_mixed_filter.json` |
| Table 9 (Appendix G) z=2 w=0.4, two parts | 0.1678 | `restricted/restricted_z2_W0.4_d6_mixed_filter_parts2.json` |
| Table 9 (Appendix G) z=2 w=0.4, two parts, d | 6 | `restricted/restricted_z2_W0.4_d6_mixed_filter_parts2.json` |
| Table 9 (Appendix G) z=2 w=0.6, two parts | 0.1805 | `restricted/restricted_z2_W0.6_d11_mixed_filter_parts2.json` |
| Table 9 (Appendix G) z=2 w=0.6, two parts, d | 11 | `restricted/restricted_z2_W0.6_d11_mixed_filter_parts2.json` |
| Table 9 (Appendix G) z=2 w=0.8, two parts | 0.1931 | `restricted/restricted_z2_W0.8_d9_mixed_filter_parts2.json` |
| Table 9 (Appendix G) z=2 w=0.8, two parts, d | 9 | `restricted/restricted_z2_W0.8_d9_mixed_filter_parts2.json` |
| Table 9 (Appendix G) z=4 w=0.4, two parts | 0.2849 | `restricted/restricted_z4_W0.4_d3_mixed_filter.json` |
| Table 9 (Appendix G) z=4 w=0.4, two parts, d | 3 | `restricted/restricted_z4_W0.4_d3_mixed_filter.json` |
| Table 9 (Appendix G) z=4 w=0.6, two parts | 0.3721 | `restricted/restricted_z4_W0.6_d3_mixed_filter_parts2.json` |
| Table 9 (Appendix G) z=4 w=0.6, two parts, d | 3 | `restricted/restricted_z4_W0.6_d3_mixed_filter_parts2.json` |
| Appendix H, q=47, Alg. isd | 0.3580 | `lee/lee_q47_full_R0.55_d7_filter.json` |
| Appendix H, q=47, Alg. isd, depth | 7 | `lee/lee_q47_full_R0.55_d7_filter.json` |
| Table 10 (Appendix H) q=47 full, no filters (d=6) | 0.4058 | `lee/lee_q47_full_R0.48_d6_exact.json` |
| Table 10 (Appendix H) q=47 full, no filters, depth | 6 | `lee/lee_q47_full_R0.48_d6_exact.json` |
| Table 10 (Appendix H) q=49 half, no filters (d=4) | 0.2851 | `lee/lee_q49_half_R0.4775_d4_exact.json` |
| Table 10 (Appendix H) q=49 half, no filters, depth | 4 | `lee/lee_q49_half_R0.4775_d4_exact.json` |
| Table 10 (Appendix H) q=4 half, no filters (d=2) | 0.0991 | `lee/lee_q4_half_R0.46_d2_exact.json` |
| Table 10 (Appendix H) q=4 half, no filters, depth | 2 | `lee/lee_q4_half_R0.46_d2_exact.json` |
| Table 10 (Appendix H) q=4 half, with filters (d=2) | 0.0950 | `lee/lee_q4_half_R0.46_d2_mixed.json` |
| Table 10 (Appendix H) q=4 half, with filters, depth | 2 | `lee/lee_q4_half_R0.46_d2_mixed.json` |
| Table 10 (Appendix H) q=47 full, with filters | 0.3580 | `lee/lee_q47_full_R0.55_d7_filter.json` |
| Table 10 (Appendix H) q=47 full, with filters, d | 7 | `lee/lee_q47_full_R0.55_d7_filter.json` |
| Table 10 (Appendix H) q=47 full, two parts | 0.3580 | `lee/lee_q47_full_R0.55_d7_filter.json` |
| Table 10 (Appendix H) q=49 half, with filters | 0.2582 | `lee/lee_q49_half_R0.51_d4_filter.json` |
| Table 10 (Appendix H) q=49 half, with filters, d | 4 | `lee/lee_q49_half_R0.51_d4_filter.json` |
| Table 10 (Appendix H) q=49 half, two parts | 0.2582 | `lee/lee_q49_half_R0.51_d4_filter.json` |
| Appendix I | 0.212 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Appendix I | 0.2572 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Appendix I | 0.1286 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Appendix I, depth 6 at the same memory | 0.2637 | `subsetsum/subsetsum_digits-3to3_d6_filter_parts2_M0.212.json` |
| Appendix I, depth 8 at memory 0.211 | 0.2621 | `subsetsum/subsetsum_digits-3to3_d8_filter_parts2_M0.211.json` |
| Appendix I, depth 8 at memory 0.211 | 0.211 | `subsetsum/subsetsum_digits-3to3_d8_filter_parts2_M0.211.json` |
| Appendix I, share of the first part | 56% | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), share of the first part | 56.01% | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), share of the second part | 43.99% | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, L, level 0 | 0.2040 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, L, level 1 | 0.2070 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, L, level 2 | 0.2086 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, L, level 3 | 0.2099 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, L, level 4 | 0.2120 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, L, level 5 | 0.1926 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, L, level 6 | 0.2120 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, ell, level 0 | 0.3103 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, ell, level 1 | 0.1957 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, ell, level 2 | 0.1808 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, ell, level 3 | 0.1524 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, ell, level 4 | 0.1004 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, ell, level 5 | 0.0604 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, ell, level 6 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, r, level 1 | 0.2990 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, r, level 2 | 0.5202 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, r, level 3 | 0.7004 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, r, level 4 | 0.8449 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, r, level 5 | 0.9396 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, r, level 6 | 0.9467 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), both parts, r, level 7 | 1.1065 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-3, level 0 | 0.00002 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-3, level 1 | 0.00002 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-3, level 2 | 0.00001 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-3, level 3 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-3, level 4 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-3, level 5 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-3, level 6 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-3, level 7 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-2, level 0 | 0.00004 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-2, level 1 | 0.00004 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-2, level 2 | 0.00003 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-2, level 3 | 0.00002 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-2, level 4 | 0.00001 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-2, level 5 | 0.00003 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-2, level 6 | 0.00010 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-2, level 7 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-1, level 0 | 0.00277 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-1, level 1 | 0.00535 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-1, level 2 | 0.00982 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-1, level 3 | 0.01689 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-1, level 4 | 0.02551 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-1, level 5 | 0.02941 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-1, level 6 | 0.03132 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_-1, level 7 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_0, level 0 | 0.99042 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_0, level 1 | 0.98137 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_0, level 2 | 0.96465 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_0, level 3 | 0.93491 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_0, level 4 | 0.88646 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_0, level 5 | 0.81621 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_0, level 6 | 0.69054 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_0, level 7 | 0.50000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_1, level 0 | 0.00669 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_1, level 1 | 0.01317 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_1, level 2 | 0.02545 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_1, level 3 | 0.04815 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_1, level 4 | 0.08802 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_1, level 5 | 0.15423 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_1, level 6 | 0.27456 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_1, level 7 | 0.50000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_2, level 0 | 0.00004 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_2, level 1 | 0.00004 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_2, level 2 | 0.00003 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_2, level 3 | 0.00002 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_2, level 4 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_2, level 5 | 0.00012 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_2, level 6 | 0.00348 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_2, level 7 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_3, level 0 | 0.00002 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_3, level 1 | 0.00002 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_3, level 2 | 0.00001 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_3, level 3 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_3, level 4 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_3, level 5 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_3, level 6 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, p_3, level 7 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, c, level 1 | 0.0013 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, c, level 2 | 0.0024 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, c, level 3 | 0.0054 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, c, level 4 | 0.0151 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, c, level 5 | 0.0400 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, c, level 6 | 0.0446 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, c, level 7 | 0.2714 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, u, level 1 | 0.5000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, u, level 2 | 0.5000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, u, level 3 | 0.5000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, u, level 4 | 0.5000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, u, level 5 | 0.5000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, u, level 6 | 0.0031 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, u, level 7 | 0.9785 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, alpha, level 1 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, alpha, level 2 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, alpha, level 3 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, alpha, level 4 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, alpha, level 5 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, alpha, level 6 | 0.0110 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, alpha, level 7 | 0.0592 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_x, level 1 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_x, level 2 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_x, level 3 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_x, level 4 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_x, level 5 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_x, level 6 | 0.0073 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_x, level 7 | 0.0472 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_y, level 1 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_y, level 2 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_y, level 3 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_y, level 4 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_y, level 5 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_y, level 6 | 0.0067 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), first part, beta_y, level 7 | 0.0439 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-3, level 0 | 0.00011 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-3, level 1 | 0.00017 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-3, level 2 | 0.00060 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-3, level 3 | 0.00103 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-3, level 4 | 0.00020 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-3, level 5 | 0.00001 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-3, level 6 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-3, level 7 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-2, level 0 | 0.00070 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-2, level 1 | 0.00836 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-2, level 2 | 0.02205 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-2, level 3 | 0.03325 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-2, level 4 | 0.02668 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-2, level 5 | 0.00793 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-2, level 6 | 0.00212 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-2, level 7 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-1, level 0 | 0.11867 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-1, level 1 | 0.18088 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-1, level 2 | 0.22024 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-1, level 3 | 0.23261 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-1, level 4 | 0.23606 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-1, level 5 | 0.20365 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-1, level 6 | 0.11819 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_-1, level 7 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_0, level 0 | 0.75714 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_0, level 1 | 0.61391 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_0, level 2 | 0.50093 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_0, level 3 | 0.44134 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_0, level 4 | 0.42399 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_0, level 5 | 0.46731 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_0, level 6 | 0.52905 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_0, level 7 | 0.50000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_1, level 0 | 0.12256 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_1, level 1 | 0.18758 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_1, level 2 | 0.23129 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_1, level 3 | 0.25142 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_1, level 4 | 0.27403 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_1, level 5 | 0.29775 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_1, level 6 | 0.32897 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_1, level 7 | 0.50000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_2, level 0 | 0.00071 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_2, level 1 | 0.00891 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_2, level 2 | 0.02423 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_2, level 3 | 0.03904 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_2, level 4 | 0.03859 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_2, level 5 | 0.02324 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_2, level 6 | 0.02154 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_2, level 7 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_3, level 0 | 0.00011 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_3, level 1 | 0.00018 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_3, level 2 | 0.00067 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_3, level 3 | 0.00132 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_3, level 4 | 0.00044 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_3, level 5 | 0.00011 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_3, level 6 | 0.00013 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, p_3, level 7 | 0 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, c, level 1 | 0.0105 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, c, level 2 | 0.0526 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, c, level 3 | 0.1180 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, c, level 4 | 0.2251 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, c, level 5 | 0.3377 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, c, level 6 | 0.3370 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, c, level 7 | 0.6183 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, u, level 1 | 0.5000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, u, level 2 | 0.5000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, u, level 3 | 0.5000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, u, level 4 | 0.5000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, u, level 5 | 0.5000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, u, level 6 | 0.5030 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, u, level 7 | 0.5065 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, alpha, level 1 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, alpha, level 2 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, alpha, level 3 | 0.1209 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, alpha, level 4 | 0.3334 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, alpha, level 5 | 0.4582 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, alpha, level 6 | 0.5815 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, alpha, level 7 | 0.5202 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_x, level 1 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_x, level 2 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_x, level 3 | 0.0816 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_x, level 4 | 0.2367 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_x, level 5 | 0.3446 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_x, level 6 | 0.4286 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_x, level 7 | 0.4217 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_y, level 1 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_y, level 2 | 0.0000 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_y, level 3 | 0.0816 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_y, level 4 | 0.2367 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_y, level 5 | 0.3446 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_y, level 6 | 0.4293 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
| Table 11 (Appendix I), second part, beta_y, level 7 | 0.4260 | `subsetsum/subsetsum_digits-3to3_d7_filter_parts2_M0.212.json` |
