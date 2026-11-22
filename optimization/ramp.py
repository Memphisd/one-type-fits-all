"""Prices tied into a small family first, then all prices free (inventory: strategies 16 and 17, the restricted rows).

    python3 optimization/ramp.py                   the example below (restricted errors over F_157, ~5 minutes)
    python3 -m jointtrees verify --import optimization/ramp.py FILE.json      a witness that uses RampFilter

A syndrome filter over F_157 has one price per class {a, -a} of Z_157 for each list: 2 x 78 variables.  The
restricted rows were first optimized with the prices on a straight line in the Lee weight r of the class,
z_r = jump - slope * r (four variables), and then with all prices free, started from the line.  RampFilter is that
family: a filter family is all it takes to tie parameters, and `optimize` starts the free family from the tied one by
itself (starts.embed takes the old family's prices).
"""
from dataclasses import dataclass

from common import run, say, stable
from jointtrees import Filter, Join, PriceFilter, RestrictedDecoding, Tree, Variable


@dataclass(frozen=True)
class RampFilter(Filter):
    """Own prices for each list on a straight line in the Lee weight r of the digit: z_r = jump - slope * r (r >= 1) and
    z_y_r = jump_y - slope_y * r.  The digit 0 has price 0."""
    name = 'ramp'
    tilt = 'own'
    u: object = 'free'

    def variables(self, ctx):
        jumps = [Variable((key,), -20.0, 20.0, ('low', 'high')) for key in ('jump', 'jump_y')]
        return jumps + [Variable((key,), -0.5, 0.5, ('low', 'high')) for key in ('slope', 'slope_y')]

    def prices(self, ctx, p):
        def line(jump, slope):
            return {j: 0.0 if j == 0 else p[jump] - p[slope] * abs(ctx.value(j)) for j in ctx.digits}
        return line('jump', 'slope'), line('jump_y', 'slope_y')

    def random_start(self, ctx, rng, shared):
        return {('jump',): rng.uniform(1, 4), ('jump_y',): rng.uniform(1, 4),
                ('slope',): rng.uniform(0, 0.1), ('slope_y',): rng.uniform(0, 0.1)}


def ramp_then_free(problem, depth, starts=4, log=None):
    """The mixed top join of `depth` with a RampFilter syndrome filter, then with free prices (PriceFilter('own'))
    from it."""
    tied = stable(run(problem, Tree.same_joins(depth=depth, top=Join(syndrome=RampFilter())), starts=starts))
    say(f'prices on a line: {tied.time:.9f}', log)
    free = stable(run(problem, Tree.same_joins(depth=depth, top=Join(syndrome=PriceFilter('own'))), warm=tied,
                      starts=0))
    say(f'all prices free, from the line: {free.time:.9f}', log)
    return free


if __name__ == '__main__':
    result = ramp_then_free(RestrictedDecoding(q=157, rate=0.5, E=(1, 156), weight=0.4), depth=2)
    print(f'{result.time:.6f} bits = {result.evaluation.F:.6f} in base 157')
