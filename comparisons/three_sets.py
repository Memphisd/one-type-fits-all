"""Appendix, comparison with [HG26]: subset sum with filters that divide the positions into three sets instead of two.

Printed:
    digits -1..2, depth 5, three sets at every join                               (paragraph Subset Sum)
    digits -2..2, depth 6, the positions partitioned into two parts, three sets   (paragraph Filters with Three Sets)
    the gain of the second tree against the best tree with two sets (digits -3..3, depth 6, two parts), rounded down

A filter of the paper divides the positions into two sets, a center of size u and its complement.  A filter of [HG26]
divides them into k sets.  In the most frequent way in which the k sets accept a consistent pair, the share of the
positions with the digits (i, j) that lies in set s is

    theta_ij(s) = 2^(c_s + a_s(i) + b_s(j)) / sum_t 2^(c_t + a_t(i) + b_t(j)),     set 0 with c_0 = a_0 = b_0 = 0,

with an offset c_s and prices a_s(i) for the first list and b_s(j) for the second list.  For k = 2, set 1 is the
center: theta_ij(1) is the fraction theta_ij of [closed form], with c the offset and a = z, b = -z the prices of the
opposite tilt.  (In [HG26] the sets are the buckets of a bucketing code, our theta_ij(s) is their share of a bucket.)

Let X and Y be the digits of the two vectors at a position and S its set, with the joint law J_ij theta_ij(s).  The
exponents of [HG26, Prop. 3] are the mutual informations of S with (X, Y), with X and with Y:

    alpha  = H(S) + H(X, Y) - H(X, Y, S)
    beta_x = H(S) + H(X) - H(X, S)
    beta_y = H(S) + H(Y) - H(Y, S)

For k = 2 they are the center count and the list reductions of [filter exponents]; the script checks this against
the library before it computes anything.  A filtered join then costs [filtered join] with these exponents, summed over
the parts of the positions.

Each data file (data/three_sets/) holds a tree of jointtrees whose filters keep every vector, and the sets of the
three-set filter of every join and part.  The library evaluates the tree: list sizes, label bits, repetitions and,
for every join and part, its size and joint type J.  The script then recomputes the cost of every filtered join with
the three-set exponents.

Run from this folder (standard library and jointtrees, a few seconds):

    python3 three_sets.py
"""
import json
import os
import sys

from jointtrees import Witness

from common import H, round_down, shown

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data', 'three_sets')
WITNESSES = os.path.join(HERE, '..', 'witnesses', 'subsetsum')

CHECK_TREE = 'subsetsum_digits-1to2_d5_filter.json'           # a two-set tree for the check against the library
BEST_TWO_SETS = 'subsetsum_digits-3to3_d6_filter_parts2.json'    # the best tree with two sets: 0.2620, depth 6


def exponents(J, shares):
    """alpha, beta_x, beta_y of a filter on a part with joint type J = {(i, j): share}, where shares[i, j] lists the
    shares theta_ij(0), ..., theta_ij(k-1) of the positions (i, j) in the sets 0, ..., k-1."""
    XYS, S, XS, YS, X, Y = {}, {}, {}, {}, {}, {}
    for (i, j), m in J.items():
        for s, t in enumerate(shares[i, j]):
            v = m * t
            XYS[i, j, s] = v
            S[s] = S.get(s, 0.0) + v
            XS[i, s] = XS.get((i, s), 0.0) + v
            YS[j, s] = YS.get((j, s), 0.0) + v
        X[i] = X.get(i, 0.0) + m
        Y[j] = Y.get(j, 0.0) + m
    return H(S) + H(J) - H(XYS), H(S) + H(X) - H(XS), H(S) + H(Y) - H(YS)


def set_shares(J, sets):
    """theta_ij(s) for every pair (i, j) of J.  `sets` lists the sets 1, ..., k-1 as {'c': offset, 'a': prices of
    the first list, 'b': prices of the second list}, the prices keyed by the digit as a string (missing: price 0)."""
    shares = {}
    for i, j in J:
        scores = [0.0] + [s['c'] + s['a'].get(str(i), 0.0) + s['b'].get(str(j), 0.0) for s in sets]
        top = max(scores)
        weights = [2.0 ** (x - top) for x in scores]
        shares[i, j] = [x / sum(weights) for x in weights]
    return shares


def check_two_sets():
    """For k = 2 the exponents above must be the library's [filter exponents]: every filtered join of a two-set tree,
    with its offset c and the prices a = z, b = -z of the opposite tilt."""
    witness = Witness.load(os.path.join(WITNESSES, CHECK_TREE))
    evaluation = witness.evaluate()
    for i, join in enumerate(evaluation.joins):
        for record in join['filters']:
            if record['kind'] == 'none':
                continue
            z = witness.parameters.filter[i]['z']
            sets = [{'c': record['offset'], 'a': {str(a): v for a, v in z.items()},
                     'b': {str(a): -v for a, v in z.items()}}]
            ours = exponents(record['J'], set_shares(record['J'], sets))
            library = (record['alpha'], record['beta_x'], record['beta_y'])
            if max(abs(x - y) for x, y in zip(ours, library)) > 1e-9:
                sys.exit(f'{CHECK_TREE}, join {i}: alpha, beta_x, beta_y {ours} differ from the library {library}')


def tree_time(name):
    """The time exponent of the tree of a data file, with its filters of three sets."""
    with open(os.path.join(DATA, name + '.json')) as handle:
        data = json.load(handle)
    evaluation = Witness.from_dict(data['witness']).evaluate()
    if not evaluation.feasible:
        sys.exit(f'{name}: the tree violates {sorted(evaluation.violations)}')
    filters = {(f['join'], f['part']): f['sets'] for f in data['filters']}
    d = len(evaluation.L) - 1
    time = 0.0
    for i in range(d + 1):
        records = [r for r in evaluation.joins[i]['filters'] if r['kind'] != 'none']    # the parts filtered at join i
        if sorted(r['part'] for r in records) != sorted(part for join, part in filters if join == i):
            sys.exit(f'{name}: join {i} of the tree and the data file filter different parts')
        if not records:                                        # a join without filter: the library's cost
            time = max(time, evaluation.T[i] + evaluation.Delta[i])
            continue
        alpha = beta_x = beta_y = 0.0
        for r in records:                                      # the exponents add up over the parts
            a, bx, by = exponents(r['J'], set_shares(r['J'], filters[i, r['part']]))
            alpha, beta_x, beta_y = alpha + r['size'] * a, beta_x + r['size'] * bx, beta_y + r['size'] * by
        L, ell = evaluation.L[i - 1], evaluation.joins[i]['ell']
        terms = [L + alpha - beta_x, L + alpha - beta_y, 2 * L - ell + alpha - beta_x - beta_y]
        if i < d:
            terms.append(evaluation.L[i])                      # writing the output list
        time = max(time, max(terms) + evaluation.Delta[i])
    return time + evaluation.runs


def main():
    check_two_sets()
    four = tree_time('subsetsum_digits-1to2_d5')
    parts = tree_time('subsetsum_digits-2to2_d6_parts2')
    two_sets = Witness.load(os.path.join(WITNESSES, BEST_TWO_SETS)).evaluate().time
    print(f'Appendix D, digits -1..2, depth 5, three sets                    {shown(four)}  ({four:.9f})')
    print(f'Appendix D, digits -2..2, depth 6, two parts, three sets         {shown(parts)}  ({parts:.9f})')
    print(f'Appendix D, gain against two sets (digits -3..3, depth 6)        {shown(two_sets - parts, rounding=round_down)}  '
          f'({two_sets:.9f} - {parts:.9f})')


if __name__ == '__main__':
    main()
