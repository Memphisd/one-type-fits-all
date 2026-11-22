# Optimization strategies

The scripts of this folder are strategies for optimizing trees, each written on top of the library jointtrees. The
table lists the strategies and where each one is: in the library or in a script of this folder.

The scripts import `jointtrees` and nothing else outside this folder. Install the library as in the README one folder
up.

| # | strategy | here |
|---|---|---|
| 1 | one join level more (or less) at the bottom | `jointtrees.starts.deeper`, `deepen.py` |
| 2 | a new feature switched on at its neutral value | `starts.embed`, `new_feature.py` |
| 3 | a new feature seeded at active values | edit the parameters and pass them as warm starts (`new_feature.py`) |
| 4 | another filter family as a start (a tied family to free prices) | `starts.embed` (also used by `optimize` for a start of another tree) |
| 5 | more digits for the lists | `jointtrees.starts.with_digits`, `more_digits.py` |
| 6 | optima of several tree variants as starts | a list of warm starts (`new_feature.py`) |
| 7 | a start built to be feasible | build parameters by hand (`examples/parameters.py`) |
| 8 | warm starts across rates, memory bounds, q | `problem.replace(...)`, `worst_rate.py`, `tradeoff.py` |
| 9 | one part copied into two | `jointtrees.starts.into_parts`, `two_parts.py` |
| 10 | a denser second part | `two_parts.denser` |
| 11 | a random second part | `two_parts.random_second_part` |
| 12 | parts pushed apart by constraints, then released | `bounds={'parts[2].p[3][0]': (None, 0.5)}`, then a run without |
| 13 | a new part searched alone, then released | `fixed={'ell': ..., 'parts[1]': ...}`, `two_parts.new_part` |
| 14 | a filter center held small, then released | `fixed={'filter[j].u': 0.02}`, `common.release_centers` |
| 15 | bounds of single variables | `bounds={name: (low, high)}` |
| 16 | parameters tied into a small family | a new filter family (`ramp.py`) |
| 17 | a restricted family first, then the full one | two runs, the first as the warm start of the second (`ramp.py`) |
| 18 | a time limit per run | `optimize(time_limit=...)`, `result.cut`, `result.starts` |
| 19 | restarts until a round gains little | `polish`, `common.stable` |
| 20 | start policies | `starts`, `seed`, `warm`, `SearchSpace.random` |
| 21 | checks by more starts or perturbations | `starts`, `seed`, `result.starts`, `parallel.py` |
| 22 | searches over groups of variables in turn | `fixed=` with groups, `alternate.py` |
| 23 | a depth chain with a stop rule | `deepen.py` |
| 24 | a digit-set chain | `more_digits.py` |
| 25 | the worst case over the rate | `worst_rate.py` |
| 26 | the best of many trees, starts or stored witnesses | `common.best`, `common.best_witness` |
| 27 | parallel runs, job queues | `parallel.py` |
| 28 | a grid scan with the tree fixed | a loop over `evaluate` |

Every script runs as it is (`python3 optimization/deepen.py`) with a small example in its `__main__` part, and its
functions take any problem and tree. A script of this folder uses the others by importing them
(`from deepen import chain`), since Python puts the folder of the script it runs on the path.
