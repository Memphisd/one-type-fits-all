# Witnesses and scripts of the paper

This repository accompanies the Preprint "One Type Fits All: A General Analysis of Representation Trees for Subset
Sum, LWE and Decoding" and provides everything needed to re-compute its numbers via the jointtrees library: the witnesses of the paper's numbers, optimization
strategies for trees, the comparisons with earlier algorithms, and a check of every printed number.

## Install

The scripts use the library jointtrees 0.1, cloned next to this repository:

```sh
git clone https://github.com/Memphisd/jointtrees.git
git clone https://github.com/Memphisd/one-type-fits-all.git && cd one-type-fits-all
python3 -m venv .venv && . .venv/bin/activate     # a fresh Python environment (Python 3.9 or later)
pip install ../jointtrees                          # the library, with numpy and scipy
sh run_all.sh                                      # every check of this repository, about 3 minutes
```

## Folders

| folder | content |
|---|---|
| `witnesses/` | one witness file per tree behind a number of the paper, and `witnesses/README.md`, the index from every number to its files |
| `optimization/` | optimization strategies for trees, one script each (`optimization/README.md`) |
| `comparisons/` | the computations of earlier algorithms and of filters with three sets (`comparisons/README.md`) |
| `recompute/` | `check_numbers.py`, which recomputes every printed number from its witness, and `numbers.csv`, the list of these numbers |

## First commands

```sh
python3 -m jointtrees verify witnesses     # every witness: re-evaluation and independent checks
python3 recompute/check_numbers.py         # every printed number against its witness, a few minutes
sh run_all.sh                              # both, and every script of comparisons/, about three minutes
```

The comparisons have their own commands, see `comparisons/README.md`.
