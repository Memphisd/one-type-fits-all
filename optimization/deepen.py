"""More join levels until the exponent stops improving (inventory: strategies 1, 14, 19, 23).

    python3 optimization/deepen.py                  the example below (subset sum, digits -1..2, filters, ~10 minutes)

The chain starts at a small depth with random starts.  Every further depth d + 1 is started from the best tree of
depth d with a new lowest join (`deeper`, two ways: every digit on its simplest pair, or a copy of the old lowest
join), from a stored witness of depth d + 1 if there is one, and from a few random points.  The best of these is
made stable (restarts until a round gains less than 1e-6) and its filter centers are held small and released.
The chain stops at the first depth that does not beat the best smaller depth by more than EPS.
"""
import os

from common import best, best_witness, fresh, release_centers, run, say, stable
from jointtrees import SubsetSum, filtered
from jointtrees.starts import deeper

EPS = 1e-5          # a deeper tree must be better by more than this


def chain(problem, tree_of, first, last, result=None, starts=4, folder=None, log=None, time_limit=None):
    """The best result over the depths first..last of the family tree_of(depth).  It stops when a depth gains <= EPS.
    `result`: an optimum of the depth `first`, if known (the chain then starts one join deeper).  `folder`: stored
    witnesses to start from, and where the results are written."""
    options = {'time_limit': time_limit} if time_limit else {}
    results = {} if result is None else {first: result}
    for depth in range(first + len(results), last + 1):
        tree = tree_of(depth)
        warm = []
        if depth - 1 in results:                                    # one join more than the best smaller tree
            for new in ('balanced', 'copy'):
                try:
                    warm.append(deeper(results[depth - 1], problem, tree, new=new))
                except ValueError as error:
                    say(f'depth {depth}: no {new} start ({error})', log)
        stored = best_witness(folder, problem, tree) if folder else None
        if stored is not None:
            warm.append(stored)
        result = run(problem, tree, warm=warm or None, starts=starts, **options)
        if result is None:
            say(f'depth {depth}: no feasible point', log)
            break
        result = release_centers(stable(result, **options), **options)
        say(f'depth {depth}: {result.time:.9f}  (from {len(warm)} warm starts and {starts} more)', log)
        if folder:
            path = fresh(os.path.join(folder, f'depth_{depth}.json'))
            result.save(path, note=f'optimization/deepen.py, depth {depth}')
        previous = min((r.time for r in results.values()), default=None)
        results[depth] = result
        if previous is not None and result.time > previous - EPS:
            say(f'depth {depth} does not beat depth {depth - 1} by more than {EPS}: stop', log)
            break
    return best(*results.values())


def example_tree(depth):
    """The filtered tree of the example: every join filters, digits -1..2."""
    return filtered(depth=depth, digits=(-1, 0, 1, 2))


if __name__ == '__main__':
    winner = chain(SubsetSum(), example_tree, first=2, last=6, starts=3)
    print(f'best depth {winner.tree.depth}: {winner.time:.6f}')
