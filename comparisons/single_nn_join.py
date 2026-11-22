"""Table 4 (Section 7): the time exponent tau_nn of one nearest-neighbour join over F_q without a filter, with the center
count of Hirose [Hir16, Theorem 1], and with the filter of [neighbour join].

The join receives two lists of 2^(L n') vectors of F_q^n', both restricted to the type (1/q, ..., 1/q), and outputs
the pairs at Hamming distance gamma n'.  Such a pair has the joint type J_gamma: the share (1 - gamma)/q of the
positions for every pair (i, i) of equal digits, and gamma/(q(q - 1)) for every pair (i, j) of different digits.  L
is the value printed in the table, and tau_nn is in bits per coordinate (time 2^(tau_nn n')).

    no filter      every pair of the two lists is compared: tau_nn = 2L
    proposition    the filter of [neighbour join]: the same tilt on both lists, the price z0 on the digit 0 and 0 on
                   the other digits, center size u.  Its center count alpha and list reduction beta are the filter
                   exponents [filter exponents] on J_gamma, and the cost of the filtered join without label bits is
                   tau_nn = max(L + alpha - beta, 2L + alpha - 2 beta) [filtered join]
    Hirose         the same cost with Hirose's center count alpha_H and list reduction beta_H (common.py)

Theorem 1 of [Hir16] states the time alpha_H under the condition L <= beta_H.  The cost above allows L > beta_H as
well.  In four rows the minimum has L = beta_H, where both agree.  In the row q = 3, L = 0.1585, gamma = 0.4 the
minimum (0.284046) has L > beta_H, and under the condition L <= beta_H the minimum is 0.284133.  The table states the
first value.

Run from this folder:

    python3 single_nn_join.py              the parameters in data/single_nn_join.json, standard library only
    python3 single_nn_join.py --optimize   the minimum over the filter parameters, from 20 random starts per cell
                                           (numpy, scipy, half a minute)

Each line gives a cell of the table, rounded up as the paper rounds exponents, and its unrounded value.
"""
import json
import math
import os
import random
import sys

from common import hirose_exponents, shown, syndrome_filter_exponents

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data', 'single_nn_join.json')
COLUMNS = ('no filter', 'Hirose', 'proposition')
STARTS = 20                     # random starts per cell with --optimize


def joint_type(q, gamma):
    """J_gamma, the joint type of a pair at distance gamma n' of two vectors of the type (1/q, ..., 1/q)."""
    return {(i, j): (1 - gamma) / q if i == j else gamma / (q * (q - 1)) for i in range(q) for j in range(q)}


def join_cost(L, alpha, beta):
    """[filtered join] without label bits and with beta_x = beta_y = beta: the bucketing and the checking term."""
    return max(L + alpha - beta, 2 * L + alpha - 2 * beta)


def proposition_exponents(q, gamma, z0, u):
    """alpha and beta of the filter of [neighbour join] on J_gamma: the same prices on both lists, z0 on the digit 0
    and 0 on the other digits, center size u."""
    alpha, beta, _ = syndrome_filter_exponents(q, joint_type(q, gamma), 'same', {'u': u, 'z': {'0': z0}})
    return alpha, beta


def stored_cells(row):
    """The three exponents of a row at its stored parameters: {column: tau_nn}."""
    q, L, gamma = row['q'], row['L'], row['gamma']
    alpha, beta = proposition_exponents(q, gamma, row['proposition']['z0'], row['proposition']['u'])
    alpha_h, beta_h, theta = hirose_exponents(q, gamma, row['hirose']['u'], row['hirose']['h0'])
    if min(theta) < -1e-12 or max(theta) > 1 + 1e-12:
        raise ValueError(f'q = {q}, gamma = {gamma}: the stored center of Hirose has a fraction outside [0, 1]')
    return {'no filter': 2 * L, 'Hirose': join_cost(L, alpha_h, beta_h), 'proposition': join_cost(L, alpha, beta)}


def minimum(L, exponents, constraints, bounds, starts):
    """The smallest cost max(L + alpha - beta, 2L + alpha - 2 beta) over the parameters x of `exponents` (x -> alpha,
    beta) for which every function in `constraints` is >= 0: SLSQP on (x, t) with t above both terms, from every
    start.  A constraint function receives (x, t)."""
    import numpy as np
    from scipy.optimize import minimize

    def above_terms(y):
        alpha, beta = exponents(y[:-1])
        return np.array([y[-1] - L - alpha + beta, y[-1] - 2 * L - alpha + 2 * beta])

    def last(y):
        return y[-1]

    conditions = [{'type': 'ineq', 'fun': above_terms}] + [{'type': 'ineq', 'fun': c} for c in constraints]
    best = math.inf
    for x in starts:
        start = list(x) + [join_cost(L, *exponents(x))]
        y = minimize(last, start, method='SLSQP', bounds=bounds + [(None, None)], constraints=conditions,
                     options={'ftol': 1e-14, 'maxiter': 500}).x
        if all(c(y) >= -1e-10 for c in constraints):
            best = min(best, join_cost(L, *exponents(y[:-1])))
    return best


def optimized_cells(row, rng):
    """The three exponents of a row, minimized over the filter parameters from random starts."""
    q, L, gamma = row['q'], row['L'], row['gamma']

    def proposition(x):                                     # x = (z0, u)
        return proposition_exponents(q, gamma, x[0], x[1])

    def hirose(x):                                          # x = (u, h0)
        return hirose_exponents(q, gamma, x[0], x[1])[:2]

    def lowest_fraction(y):
        return min(hirose_exponents(q, gamma, y[0], y[1])[2])

    def highest_fraction(y):
        return 1 - max(hirose_exponents(q, gamma, y[0], y[1])[2])

    starts = [(rng.uniform(0.1, 8.0), rng.uniform(0.01, 0.99)) for _ in range(STARTS)]
    value = minimum(L, proposition, [], [(-40.0, 40.0), (0.001, 0.999)], starts)
    starts = []
    while len(starts) < STARTS:
        x = (rng.uniform(0.01, 0.99), rng.uniform(0.0, 1.0))
        if lowest_fraction(x) >= 0 and highest_fraction(x) >= 0:
            starts.append(x)
    value_h = minimum(L, hirose, [lowest_fraction, highest_fraction], [(1e-6, 1 - 1e-6), (0.0, 1.0)], starts)
    return {'no filter': 2 * L, 'Hirose': value_h, 'proposition': value}


def main():
    with open(DATA) as handle:
        rows = json.load(handle)['rows']
    optimize = '--optimize' in sys.argv[1:]
    rng = random.Random(1)
    for row in rows:
        values = optimized_cells(row, rng) if optimize else stored_cells(row)
        for column in COLUMNS:
            label = f"Table 4, q = {row['q']}, L = {row['L']}, gamma = {row['gamma']:.2f}, {column}"
            print(f'{label:56s} {shown(values[column])}  ({values[column]:.9f})')


if __name__ == '__main__':
    main()
