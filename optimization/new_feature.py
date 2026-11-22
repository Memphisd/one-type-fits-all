"""Switching on a new feature of the tree (inventory: strategies 2, 3, 6, the mixed top join of the decoders).

    python3 optimization/new_feature.py             the example below (F_11, half distance, depth 1, ~5 minutes)

A tree with a new feature (here the mixed top join, which matches some syndrome coordinates exactly and the rest by
distance) contains simpler trees: with ℓ^(d) = 0 it is the nearest-neighbour join, with its syndrome filter switched
off it is the exact top join.  Their optima are starts for it: `embed` keeps what matches by name and switches every
new feature on at its neutral value, so the start has exactly the old time (the script checks it).  Starts with the
feature already active (seeded values of the syndrome filter) are tried as well, and the best result is kept.
"""
import copy

from common import best, run, say, stable
from jointtrees import Decoding, Join, PriceFilter, Record, Tree, evaluate
from jointtrees.algorithms import mixed_top
from jointtrees.starts import embed


def with_new_feature(problem, tree, simpler, seeds=(), starts=2, log=None):
    """The best result for `tree` from the optima of the `simpler` trees (each checked to keep its time as a start)
    and from `seeds` (functions that edit a copy of the best start)."""
    warm = []
    for old in simpler:
        start = embed(old, problem, tree)                   # the old optimum written for the new tree
        assert abs(evaluate(problem, tree, start).time - old.time) < 1e-9, 'the new tree does not contain the old one'
        optimized = run(problem, tree, starts=0, warm=start)
        found = optimized.time if optimized else float('nan')
        say(f'from {old.tree!r}: start {old.time:.9f}, optimized {found:.9f}', log)
        warm += [start] + ([optimized] if optimized is not None else [])
    for seed in seeds:
        P = copy.deepcopy(best(*[w for w in warm if hasattr(w, 'time')]).parameters)
        seed(P)
        warm.append(P)
    result = run(problem, tree, warm=warm, starts=starts)
    say(f'{tree!r}: {result.time:.9f}', log)
    return stable(result)


if __name__ == '__main__':
    code = Decoding(q=11, rate=0.494, weight='gv/2')
    nn = stable(run(code, Tree([Join(), Join(exact=False, syndrome=PriceFilter('own'))]), starts=4))
    exact = stable(run(code, Tree([Join(), Join()]), starts=4))

    def active_filter(P, z=3.5, u=0.25):                    # a seed: the syndrome filter already on
        P.syndrome_filter = Record(z={0: z}, z_y={0: z}, u=u)

    result = with_new_feature(code, mixed_top(1), [nn, exact], seeds=[active_filter])
    print(f'mixed top join: {result.time:.6f} bits = {result.evaluation.F:.6f} in base 11')
