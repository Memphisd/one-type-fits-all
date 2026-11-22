"""From one part to two parts (inventory: strategies 9 to 13, the partitioning results of the paper).

    python3 optimization/two_parts.py               the example below (subset sum, digits -1..1, depth 3, ~15 minutes)

The example ends at the one-part value 0.284316.  Two parts reach 0.284285 there, found from 8 of 181 random
two-part starts.

The one-part optimum copied into two parts has the same exponent and is a fixed point of the local search, so the
second part has to be pushed away from the first.  The starts of `two_parts`:

  copies     the optimum in both parts, with part sizes 0.3, 0.5, 0.7                               (strategy 9)
  denser     part 2 puts more of every digit on pairs of non-zero digits (factor F), part 1 less     (strategy 10)
  random     part 1 the optimum, part 2 a random point of the search                                (strategy 11)
  new part   part 2 at a small size w: its parameters are searched alone with ℓ and part 1 held,
             then everything is released                                                           (strategy 13)
"""
import copy

import numpy as np

from common import best, run, say, stable
from jointtrees import SearchSpace, SubsetSum, filtered
from jointtrees.starts import embed, into_parts


def denser(P, factor, problem, tree):
    """Part 2 writes every parent digit more often as a pair of non-zero digits (shares times `factor`), part 1 less
    (divided by it).  The shares of each parent digit are scaled back to their sum.  Returned as parameters of `tree`
    whose joint types fit their levels again."""
    add = problem.add
    P = copy.deepcopy(P)
    for k, f in ((1, 1 / factor), (2, factor)):
        for J in P.parts[k].J.values():
            for s in {add(a, b) for a in J for b in J[a]}:
                pairs = [(a, b) for a in J for b in J[a] if add(a, b) == s and J[a][b] > 0]
                total = sum(J[a][b] for a, b in pairs)
                scaled = {(a, b): J[a][b] * (f if a != 0 and b != 0 else 1.0) for a, b in pairs}
                norm = sum(scaled.values())
                for (a, b), m in scaled.items():
                    J[a][b] = m * total / norm if norm > 0 else J[a][b]
    return embed(P, problem, tree)                      # the shares per parent digit, applied from the top down


def random_second_part(problem, tree, P, seed):
    """Part 1 and the shared values from P, part 2 from a random point of the search."""
    space = SearchSpace(problem, tree)
    rng = np.random.default_rng(seed)
    for _ in range(20):
        x = space.random(rng)
        if space.evaluate(x) is not None:
            out = copy.deepcopy(P)
            out.parts[2] = space.parameters(x).parts[2]
            return out
    return None


def new_part(problem, tree, one, size=0.05, starts=6):
    """Strategy 13: part 2 at a small size, its parameters searched with ℓ and part 1 held, then everything released.
    With ℓ and part 1 held, the new part must lower every cost term that sets the time and meet every tight constraint
    on its own."""
    P = into_parts(one, sizes=[1 - size])
    held = run(problem, tree, warm=P, starts=starts, fixed={'ell': P.ell, 'parts[1]': P.parts[1]})
    return run(problem, tree, warm=held, starts=0) if held is not None else None


def two_parts(problem, tree_one, one=None, starts=4, log=None):
    """The best two-part result for `tree_one` (one part) on `problem`.  `one`: its one-part optimum, if known."""
    one = one or stable(run(problem, tree_one, starts=starts))
    tree = tree_one.replace(parts=2)
    warm = [into_parts(one, sizes=[s]) for s in (0.3, 0.5, 0.7)]
    warm += [denser(into_parts(one, sizes=[0.5]), factor, problem, tree) for factor in (2, 4, 8)]
    warm += [w for w in (random_second_part(problem, tree, into_parts(one), seed) for seed in (1, 2)) if w is not None]
    two = run(problem, tree, warm=warm, starts=starts)
    say(f'one part {one.time:.9f}, two parts from {len(warm)} starts: {two.time if two else float("nan"):.9f}', log)
    priced = new_part(problem, tree, one)
    say(f'two parts from a new part: {priced.time if priced else float("nan"):.9f}', log)
    return stable(best(two, priced))


if __name__ == '__main__':
    result = two_parts(SubsetSum(), filtered(depth=3, digits=(-1, 0, 1)))
    print(f'two parts: {result.time:.6f}, part sizes {[part["size"] for part in result.evaluation.parts.values()]}')
