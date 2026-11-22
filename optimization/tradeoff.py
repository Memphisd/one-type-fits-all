"""A time-memory trade-off curve (inventory: strategy 8, the trade-off figures).

    python3 optimization/tradeoff.py                the example below (subset sum, 7-dissection, filters, ~10 minutes)

Memory bounds are run from the largest to the smallest, each started from the optimum at the bound before it
(a larger bound: that optimum may not fit the new bound and is repaired) and from random points.  A second pass
starts every bound from both neighbours until no point improves.
"""
from common import run, say
from jointtrees import Join, PriceFilter, SubsetSum, Tree


def tradeoff(problem, tree, memory_bounds, starts=2, log=None):
    """{memory bound: Result} for the given memory bounds."""
    bounds = sorted(memory_bounds, reverse=True)                            # largest first
    results = {}
    for k, M in enumerate(bounds):                                          # first pass: from the larger neighbour
        warm = results.get(bounds[k - 1]) if k else None
        results[M] = run(problem, tree, memory_bound=M, warm=warm, starts=starts)
        say(f'M = {M}: {results[M].time if results[M] else float("nan"):.9f}', log)
    changed = True
    while changed:                                                          # second pass: from both neighbours
        changed = False
        for k, M in enumerate(bounds):
            warm = [results.get(bounds[j]) for j in (k - 1, k + 1) if 0 <= j < len(bounds) and results.get(bounds[j])]
            new = run(problem, tree, memory_bound=M, warm=warm or None, starts=0)
            if new is not None and (results[M] is None or new.time < results[M].time - 1e-9):
                results[M], changed = new, True
                say(f'M = {M}: improved to {new.time:.9f}', log)
    return results


if __name__ == '__main__':
    tree = Tree([Join(dissection=True)] + [Join(filter=PriceFilter())] * 3, digits=(-1, 0, 1, 2),
                accounting='repetitions')
    curve = tradeoff(SubsetSum(), tree, memory_bounds=[0.20, 0.15, 0.10])
    for M, result in sorted(curve.items()):
        print(f'M = {M:.3f}: time {result.time:.6f}')
