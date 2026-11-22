"""The worst case over the rate of a decoding problem (inventory: strategies 8, 25, the tables of the decoders).

    python3 optimization/worst_rate.py              the example below (F_3, half distance, May-Ozerov, ~5 minutes)

On a grid of rates around a center, each rate is optimized from the optimum at its neighbour (first pass: from the
middle upwards, then downwards).  A second pass starts every rate from both neighbours' optima until no rate
improves by more than 1e-9.  If the largest exponent lies at an end of the grid, the grid grows there and both
passes run again.  The worst case is the largest exponent on the grid.
"""
from common import run, say
from jointtrees import Decoding
from jointtrees.algorithms import may_ozerov


def worst_rate(problem, tree, center, step=0.002, width=3, starts=2, log=None, grow=3):
    """(worst rate, its Result, {rate: Result}) for `problem` (a decoding problem, whose rate is replaced) on
    `tree`."""
    rates = [round(center + k * step, 10) for k in range(-width, width + 1)]
    results = {}

    def solve(rate, warm, starts):
        result = run(problem.replace(rate=rate), tree, warm=[w for w in warm if w is not None] or None, starts=starts)
        if result is not None and (rate not in results or result.time < results[rate].time - 1e-12):
            results[rate] = result
            return True
        return False

    for _ in range(grow + 1):
        middle = len(rates) // 2
        for k in list(range(middle, len(rates))) + list(range(middle - 1, -1, -1)):     # first pass
            if rates[k] not in results:
                if k > middle:
                    neighbour = results.get(rates[k - 1])
                elif k < middle:
                    neighbour = results.get(rates[k + 1])
                else:
                    neighbour = None
                solve(rates[k], [neighbour], starts)
        changed = True
        while changed:                                                                   # second pass
            changed = False
            for k, rate in enumerate(rates):
                neighbours = [results.get(rates[j]) for j in (k - 1, k + 1) if 0 <= j < len(rates)]
                changed |= solve(rate, neighbours, 0)
        worst = max((r for r in rates if r in results), key=lambda r: results[r].time)
        say(f'grid {rates[0]:.4f}..{rates[-1]:.4f}: worst rate {worst:.4f}, exponent {results[worst].time:.6f} '
            'bits', log)
        if worst not in (rates[0], rates[-1]):
            break
        extra = [round(worst + (k if worst == rates[-1] else -k) * step, 10) for k in range(1, width + 1)]
        rates = sorted(set(rates) | {r for r in extra if 0 < r < 1})
    return worst, results[worst], results


if __name__ == '__main__':
    rate, result, curve = worst_rate(Decoding(q=3, rate=0.46, weight='gv/2'), may_ozerov(2), center=0.466)
    print(f'worst rate {rate}: {result.time:.6f} bits = {result.evaluation.F:.6f} in base 3')
