"""Table of restricted errors (Table 9), column "published [BBPSWW23]": the time exponents of the decoders of
[BBPSWW23] for q = 157, R = 0.5 and E = {+-1} (z = 2) or E = {+-1, +-eta} (z = 4).

[BBPSWW23] shows these exponents as curves over the weight omega (Figs. 2 and 3 of arXiv:2303.08882), without
numbers.  This script computes them with the authors' code, github.com/sebastianbitzer/rest-dec (BJMM2.py, BJMM3.py,
macros.py), unchanged.  Its function optimize_BJMMk(q, z, R, omega, 20) runs SLSQP from random starts until a run
succeeds and returns the time in bits per n of the last run.  Here numpy's seed is fixed before each call, and a call
counts only if the point it returns satisfies every equality of the authors' model up to 1e-5 and violates every
inequality by at most 1e-5 (SLSQP stops at tol = 1e-4, and points with larger violations reach slightly lower times
that are not points of the model).

    levels   the decoder BJMM(2)+ or BJMM(3)+ of [BBPSWW23], the column d of the table

The default run repeats the stored seed of each cell (data/restricted_published.json).  --optimize tries the seeds
0, ..., 29 and keeps the lowest time.  Each line gives the time rounded to the nearest four decimals (a value of
earlier work, not an exponent of ours), the unrounded time and the seed.

    git clone https://github.com/sebastianbitzer/rest-dec
    python3 restricted_published.py rest-dec              about 30 seconds (numpy, scipy)
    python3 restricted_published.py rest-dec --optimize   about 12 minutes
"""
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data', 'restricted_published.json')
q, R = 157, 0.5
SEEDS = range(30)
TOLERANCE = 1e-5


def run(modules, z, omega, levels, seed):
    """One call of the authors' optimizer: (the time in bits per n, the largest violation of the model's constraints
    at the point it returns).  The constraints are those of the last SLSQP run, whose point the authors' function
    returns.  The time is recomputed at that point as a check."""
    module = modules[levels]
    last = {}
    minimize = module.opt.minimize

    def recording(*args, **kwargs):
        result = minimize(*args, **kwargs)
        last.update(constraints=kwargs['constraints'], x=result.x, cost=args[0])
        return result

    module.opt.minimize = recording
    try:
        np.random.seed(seed)
        optimize = module.optimize_BJMM2 if levels == 2 else module.optimize_BJMM3
        time, _, success = optimize(q, z, R, omega, 20, False)
    finally:
        module.opt.minimize = minimize
    if abs(last['cost'](last['x']) / module.scale - time) > 1e-12:
        raise RuntimeError(f'z = {z}, omega = {omega}, seed {seed}: the returned time is not that of the last run')
    if not success:
        return time, float('inf')
    violation = 0.0
    for constraint in last['constraints']:
        value = float(constraint['fun'](last['x']))
        violation = max(violation, abs(value) if constraint['type'] == 'eq' else -value)
    return time, violation


def main():
    if len(sys.argv) < 2 or not os.path.isdir(sys.argv[1]):
        sys.exit(__doc__)
    sys.path.insert(0, os.path.abspath(sys.argv[1]))
    import BJMM2
    import BJMM3
    modules = {2: BJMM2, 3: BJMM3}
    search = '--optimize' in sys.argv
    with open(DATA) as handle:
        cells = json.load(handle)['cells']
    for cell in cells:
        z, omega, levels = cell['z'], cell['omega'], cell['levels']
        seeds = SEEDS if search else [cell['seed']]
        valid = []
        for seed in seeds:
            time, violation = run(modules, z, omega, levels, seed)
            if violation <= TOLERANCE:
                valid.append((time, seed))
        label = f'Table 9, published [BBPSWW23], z = {z}, omega = {omega}, BJMM({levels})+'
        if not valid:
            print(f'{label}: no valid run')
            continue
        time, seed = min(valid)
        print(f'{label:62s} {time:.4f}  ({time:.6f}, seed {seed})')


if __name__ == '__main__':
    main()
