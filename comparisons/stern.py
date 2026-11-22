"""Table 7, the columns Stern [Pet10] and Hirose [Hir16]: Stern's algorithm over F_q with an exact join and with
Hirose's nearest-neighbour join, at half and at full distance, for q = 2, 3, 4, 5, 7, 8, 11, 16, 27.

Decoding over F_q at rate R: the error has weight omega n, with omega the Gilbert-Varshamov weight at full distance
and half of it at half distance.  All exponents are in bits per n.  Both algorithms permute the columns at random until
the error has weight omega_1 n on the window, split the R n information columns into two halves, and enumerate on
each half the vectors of weight omega_1 n / 2 with any non-zero values.  Each of the two lists has

    L = (R/2) h(omega_1/R) + (omega_1/2) log2(q - 1)

elements.  The paper's decoder [isd] differs: its lists cover the window of kappa n = (R + ell) n columns, including
the syndrome coordinates that the joins match exactly.

    Stern    the window is the R n information columns and ell n syndrome coordinates, on which the error must be 0.
             The join matches the ell n coordinates exactly (log2 q bits each).  The permutation must place the
             weights omega_1, 0 and omega - omega_1 on the R n information columns, the ell n matched coordinates
             and the other (1 - R - ell) n coordinates, which takes

                 runs = h(omega) - R h(omega_1/R) - (1 - R - ell) h((omega - omega_1)/(1 - R - ell))

             permutations [isd].  The join reads both lists and enumerates the 2L - ell log2 q label matches
             [plain join]: time = runs + max(L, 2L - ell log2 q).
    Hirose   no exact matching (ell = 0).  The join is a nearest-neighbour join on all (1 - R) n syndrome coordinates
             at distance gamma = (omega - omega_1)/(1 - R), with Hirose's center count alpha_H and list reduction
             beta_H per coordinate (common.hirose_exponents: center size u, share h0 of the digit 0 in a center).
             By [filtered join] the time is runs + max(L, L + (1 - R)(alpha_H - beta_H),
             2L + (1 - R)(alpha_H - 2 beta_H)).

Each cell is the largest exponent over a grid of rates of step 0.002 (worst case), each rate with the smallest
exponent over the parameters.  The data file stores, per cell, the grid, the worst rate and the parameters there.

Run from this folder:

    python3 stern.py              the stored parameters at the worst rate of each cell (data/stern.json)
    python3 stern.py --optimize   the minimum at every rate of each grid and the largest of them (numpy, scipy)

Each line gives the cell, the exponent rounded up as the paper prints it, the unrounded exponent and the rate.
"""
import json
import math
import os
import random
import sys

from common import error_weight, h, hirose_exponents, shown

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data', 'stern.json')
STEP = 0.002                    # step of the grid of rates
STARTS = 6                      # random starts per rate with --optimize, besides the stored and the previous point


def list_size(q, R, omega_1):
    """L: the vectors of weight omega_1 n / 2 with non-zero values in F_q* on R n / 2 columns."""
    return R / 2 * h(omega_1 / R) + omega_1 / 2 * math.log2(q - 1)


def runs(R, omega, omega_1, ell):
    """log2 of the expected number of permutations per n: weight omega_1 on the information columns, 0 on the ell n
    matched coordinates, omega - omega_1 on the other (1 - R - ell) n."""
    rest = 1 - R - ell
    return h(omega) - R * h(omega_1 / R) - rest * h((omega - omega_1) / rest)


def stern_terms(q, R, omega, x):
    """The cost terms of Stern at x = (omega_1, ell), the permutations included."""
    omega_1, ell = x
    L = list_size(q, R, omega_1)
    extra = runs(R, omega, omega_1, ell)
    return [extra + L, extra + 2 * L - ell * math.log2(q)]


def stern_conditions(q, R, omega, x):
    """Stern needs 0 <= omega - omega_1 <= 1 - R - ell: the weight left for the coordinates outside the window."""
    omega_1, ell = x
    return [omega - omega_1, 1 - R - ell - (omega - omega_1)]


def hirose_terms(q, R, omega, x):
    """The cost terms of Stern with Hirose's nearest-neighbour join at x = (omega_1, u, h0), the permutations
    included."""
    omega_1, u, h0 = x
    L = list_size(q, R, omega_1)
    alpha, beta, _ = hirose_exponents(q, (omega - omega_1) / (1 - R), u, h0)
    extra = runs(R, omega, omega_1, 0.0)
    return [extra + L, extra + L + (1 - R) * (alpha - beta), extra + 2 * L + (1 - R) * (alpha - 2 * beta)]


def hirose_conditions(q, R, omega, x):
    """The fractions theta_i of Hirose's center lie in [0, 1], and 0 <= omega - omega_1 <= 1 - R."""
    omega_1, u, h0 = x
    theta = hirose_exponents(q, (omega - omega_1) / (1 - R), u, h0)[2]
    return [min(theta), 1 - max(theta), omega - omega_1, 1 - R - (omega - omega_1)]


MODELS = {'Stern': (stern_terms, stern_conditions, ('omega_1', 'ell')),
          'Hirose': (hirose_terms, hirose_conditions, ('omega_1', 'u', 'h0'))}


def stored_value(cell):
    """The exponent of a cell at its stored parameters (its worst rate)."""
    terms, conditions, names = MODELS[cell['column']]
    q, R = cell['q'], cell['rate']
    omega = error_weight(q, R, cell['distance'])
    x = [cell[name] for name in names]
    if min(conditions(q, R, omega, x)) < -1e-12:
        raise ValueError(f"{cell['column']}, q = {q}: the stored parameters violate a condition of the model")
    return max(terms(q, R, omega, x))


def minimum(cell, R, starts, rng):
    """The smallest exponent at the rate R and the parameters that give it: SLSQP on (x, t) with t above every cost
    term, from the given starts and random ones."""
    import numpy as np
    from scipy.optimize import minimize
    terms, conditions, names = MODELS[cell['column']]
    q = cell['q']
    omega = error_weight(q, R, cell['distance'])

    def above_terms(y):
        return np.array([y[-1] - t for t in terms(q, R, omega, y[:-1])])

    def condition(y):
        return np.array(conditions(q, R, omega, y[:-1]))

    def last(y):
        return y[-1]

    if cell['column'] == 'Stern':
        bounds = [(1e-9, min(omega, R) - 1e-9), (0.0, 1 - R)]
    else:
        bounds = [(1e-9, min(omega, R) - 1e-9), (1e-9, 1 - 1e-9), (0.0, 1.0)]
    points = [[min(max(v, low), high) for v, (low, high) in zip(x, bounds)] for x in starts]
    points = [x for x in points if min(conditions(q, R, omega, x)) >= 0]
    while len(points) < len(starts) + STARTS:
        x = [rng.uniform(low, high) for low, high in bounds]
        if min(conditions(q, R, omega, x)) >= 0:
            points.append(x)
    best, argbest = math.inf, None
    for x in points:
        y = minimize(last, x + [max(terms(q, R, omega, x))], method='SLSQP', bounds=bounds + [(None, None)],
                     constraints=[{'type': 'ineq', 'fun': above_terms}, {'type': 'ineq', 'fun': condition}],
                     options={'ftol': 1e-15, 'maxiter': 1000}).x
        if min(conditions(q, R, omega, y[:-1])) >= -1e-10:
            value = max(terms(q, R, omega, y[:-1]))
            if value < best:
                best, argbest = value, [float(v) for v in y[:-1]]
    return best, argbest


def worst_case(cell, rng):
    """The largest over the grid of rates of the smallest exponent at each rate: (value, rate, parameters).  Each
    rate starts from the stored point and from the optimum of the previous rate."""
    names = MODELS[cell['column']][2]
    low, high = cell['grid']
    rates = [round(low + k * STEP, 3) for k in range(round((high - low) / STEP) + 1)]
    stored = [[cell[name] for name in names]] if all(name in cell for name in names) else []
    previous, values = [], []
    for R in rates:
        value, x = minimum(cell, R, stored + previous, rng)
        previous = [x] if x is not None else []
        values.append((value, R, x))
    return max(values, key=lambda v: v[0])


def main():
    with open(DATA) as handle:
        cells = json.load(handle)['cells']
    optimize = '--optimize' in sys.argv[1:]
    rng = random.Random(1)
    for cell in cells:
        if optimize:
            value, R, _ = worst_case(cell, rng)
            where = f'worst rate {R:.3f} of the grid {cell["grid"][0]:.3f}..{cell["grid"][1]:.3f}'
        else:
            value, R = stored_value(cell), cell['rate']
            where = f'rate {R:.3f}'
        label = f"Table 7, {cell['column']}, q = {cell['q']}, {cell['distance']} distance"
        print(f'{label:42s} {shown(value)}  ({value:.9f}, {where})')


if __name__ == '__main__':
    main()
