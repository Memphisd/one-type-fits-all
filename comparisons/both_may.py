"""Decoding over F_q, the paragraph "Different Join Architectures" and the footnote on the algorithm of Both and May
[BM18].

The paragraph says that nearest-neighbour joins on the lower levels (Both-May) give only a tiny speedup over joins
without filter on the lower levels (May-Ozerov), and that it disappears for q >= 3.  The footnote says that the
version of the decoder [isd] with syndrome filters below the top join lowers its exponent by 2e-4 for q = 2 at full
distance and not at all for q >= 3.  Both rest on searches
that started from the decoder's trees of Table 5 (exact joins below the top join, which matches label units exactly
and filters the syndrome part, all non-zero digits alike), each at the worst rate of its cell, in which every join j
below the top may also filter a block of syndrome coordinates by distance:

    free blocks    blocks of free size at every join (q = 2 and q = 3, full distance)
    forced block   one block of at least 0.005 n, 0.02 n or 0.06 n coordinates at one join, with error weight at
                   least a tenth of that minimum, everything else free

The data file stores the end point of each search.  The script evaluates the decoder's tree of each cell (the
witnesses in ../witnesses/decoding) with jointtrees and with the model below, which must agree, and then the end
points with the model: the exponent with free blocks, and the change of the exponent against the decoder's tree with a
forced block.  It checks that every forced block has at least its minimum size and an error weight of at least a tenth
of that size, and prints both as multiples of their bounds.

The model is the decoder of [isd] with blocks.  Exponents are in bits per n, h is the binary entropy, H the entropy of
a type, and a syndrome coordinate carries b = log q bits:

    window         kappa n coordinates, kappa = R + sum_i ell^(i) / b, error weight omega_1 n, the type p^(d) with all
                   non-zero digits alike, and the joint types J^(i) of the joins 1..d.  Join 0 enumerates the two
                   halves of a base list.  [lemma 1]: r^(i) = kappa (H(J^(i)) - H(p^(i))), and the consistency loss
                   c^(i) = kappa (H(p_x) + H(p_y) - H(J^(i)))
    label units    join i matches ell^(i) bits exactly (ell^(d) at the top join)
    block j        a block of size_j n syndrome coordinates on which the error has weight w_j n.  At join j the labels
                   of the two vectors on the block must differ by a vector of the block's type t_j on level j: the
                   condition costs size_j (b - H(t_j)), and the join filters the block with a syndrome filter of its
                   own (own prices z on the digit 0 for each list, free center size u).  Above join j a list carries a
                   label of fixed type on the block, which every join splits with a joint type of its own like the
                   window: a consistency loss, and size_j (b - (H(J) - H(t))) constraints on the representations of
                   the solution [budget]
    rest           the syndrome coordinates and the error weight that are left, filtered at the top join

    [list sizes]   L^(0) = D^(0) - ell^(0) - (condition of block 0),
                   L^(i) = 2 L^(i-1) - c^(i) - ell^(i) - (condition of block i)
    [isd]          the window, the blocks in the order of their joins and the rest are taken out of the n
                   coordinates in turn.  A piece of size s and type t out of a remainder of length n' and type t'
                   costs n' H(t') - s H(t) - (n' - s) H(t'') permutations.  The window and block 0 are paid by the
                   runs of the whole tree, a block of join j >= 1 by repeating the joins j..d
    [filtered join] with the exponents alpha, beta_x, beta_y of the filters of join i [filter exponents] and the
                   output list L^(i), or [plain join] without a filter.  time = max over the cost terms + runs

Run from this folder:

    python3 both_may.py        the end points in data/both_may.json, standard library only, a second

Each line gives the exponent in bits rounded up as the paper rounds exponents, or the change of the exponent, and the
unrounded value.
"""
import json
import math
import os
import sys

from common import H, error_weight, shown, syndrome_filter_exponents
from jointtrees import Witness

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'data', 'both_may.json')
WITNESSES = os.path.join(HERE, '..', 'witnesses', 'decoding')
TOLERANCE = 1e-6                # a constraint of the model holds if its slack is above -TOLERANCE (as in verify)
BOUND_TOLERANCE = 1e-9          # tolerance of the size and weight bounds of a forced block


def weight_type(q, gamma):
    """The type of weight gamma with all non-zero digits alike."""
    return {a: 1 - gamma if a == 0 else gamma / (q - 1) for a in range(q)}


def joint_type(value, q):
    """A joint type as jointtrees writes it: a matrix over the digits, or with all non-zero digits alike the entry of
    every pair (a, b) of each case: both zero, one zero, both non-zero with sum zero or with non-zero sum."""
    if isinstance(value, list):
        return {(a, b): value[a][b] for a in range(q) for b in range(q)}
    out = {}
    for a in range(q):
        for b in range(q):
            if a == 0 and b == 0:
                case = 'both zero'
            elif a == 0 or b == 0:
                case = 'one zero'
            elif (a + b) % q == 0:
                case = 'both nonzero, sum zero'
            else:
                case = 'both nonzero, sum nonzero'
            out[a, b] = value.get(case, 0.0)
    return out


def marginals(J):
    """The types p_x and p_y of the two vectors of a joint type."""
    x, y = {}, {}
    for (a, b), m in J.items():
        x[a], y[b] = x.get(a, 0.0) + m, y.get(b, 0.0) + m
    return x, y


def split(J, parent, q, size, name):
    """[lemma 1] for a part of `size` n coordinates split by the joint type J into two vectors whose sum has the type
    `parent`: the type of the two vectors, the representations H(J) - H(parent) and the consistency loss
    H(p_x) + H(p_y) - H(J), per coordinate.  The sums of J must give `parent` up to 1e-9 / size."""
    total = {a: 0.0 for a in range(q)}
    for (a, b), m in J.items():
        total[(a + b) % q] += m
    if size * max(abs(total[a] - parent[a]) for a in range(q)) > 1e-9:
        raise ValueError(f'{name}: the joint type does not add up to the type of its level')
    x, y = marginals(J)
    return x, H(J) - H(parent), H(x) + H(y) - H(J)


def channel(t, q):
    """The joint type of two uniform labels whose difference has the type t: J_ab = t(a - b) / q."""
    return {(a, b): t[(a - b) % q] / q for a in range(q) for b in range(q)}


def exponent(q, rate, distance, depth, parameters):
    """The time exponent in bits of the decoder with blocks at `parameters` (jointtrees' names plus 'blocks'), and the
    constraints that do not hold."""
    b, d = math.log2(q), depth
    omega = error_weight(q, rate, distance)
    ell = list(parameters['ell']) + [parameters.get('ell_d', 0.0)]
    kappa = rate + sum(ell) / b
    blocks = {int(j): block for j, block in parameters.get('blocks', {}).items()}
    c, condition, fixed, slack = [0.0] * (d + 1), list(ell), list(ell), {}
    representations = demands = 0.0
    for j in range(d + 1):                                  # exact label bits: fixed on every list above their join
        demands += sum(2 ** (d - i) * ell[j] for i in range(j + 1, d + 1))
        for i in range(j + 1, d + 1):
            fixed[i] += ell[j]
    window = {d: weight_type(q, parameters['omega_1'] / kappa)}
    for i in range(d, 0, -1):                               # [lemma 1] for the window
        child, r, loss = split(joint_type(parameters['J'][str(i)], q), window[i], q, kappa, f'window, join {i}')
        window[i - 1] = child
        representations += 2 ** (d - i) * kappa * r
        c[i] += kappa * loss
    filtered = {i: [] for i in range(d + 1)}                # (size, joint type, filter) per join
    pieces = [(kappa, window[d], 0)]
    for j in sorted(blocks):                                # [lemma 1] for the blocks above their join, the condition
        block = blocks[j]
        top = weight_type(q, 0.0)                           # an empty block has weight 0 (a constraint)
        if block['size'] > 0:
            top = weight_type(q, block['weight'] / block['size'])
        t = top
        for i in range(d, j, -1):
            child, r, loss = split(joint_type(block['J'][str(i)], q), t, q, block['size'], f'block {j}, join {i}')
            c[i] += block['size'] * loss
            demands += 2 ** (d - i) * block['size'] * (b - r)
            fixed[i] += block['size'] * (b - H(t))
            t = child
        condition[j] += block['size'] * (b - H(t))
        fixed[j] += block['size'] * (b - H(t))
        filtered[j].append((block['size'], channel(t, q), block['filter']))
        pieces.append((block['size'], top, j))
        slack[f'block {j}: weight <= size'] = block['size'] - block['weight']
    rest_size = 1 - kappa - sum(block['size'] for block in blocks.values())
    rest_weight = omega - parameters['omega_1'] - sum(block['weight'] for block in blocks.values())
    rest = weight_type(q, rest_weight / rest_size)
    filtered[d].append((rest_size, channel(rest, q), parameters['syndrome_filter']))
    pieces.append((rest_size, rest, d))

    D = [kappa * H(window[i]) for i in range(d + 1)]        # [list sizes]
    half = D[0] / 2
    L = [2 * half - condition[0]]
    for i in range(1, d + 1):
        L.append(2 * L[i - 1] - c[i] - condition[i])

    runs, repeated = 0.0, [0.0] * (d + 1)                   # [isd]
    length, remaining = 1.0, weight_type(q, omega)
    for size, t, join in pieces:
        left_length = length - size
        cost = 0.0
        if left_length > 1e-12:
            left = {a: (length * remaining[a] - size * t[a]) / left_length for a in range(q)}
            cost = length * H(remaining) - size * H(t) - left_length * H(left)
            remaining = left
        length = left_length
        if join == 0:
            runs += cost
        else:
            for i in range(join, d + 1):
                repeated[i] += cost

    cost = -math.inf                                        # [plain join], [filtered join]
    for i in range(d + 1):
        L_in = half if i == 0 else L[i - 1]
        if filtered[i]:
            alpha = beta_x = beta_y = 0.0
            for size, J, f in filtered[i]:
                a, bx, by = syndrome_filter_exponents(q, J, 'own', f, size)
                alpha, beta_x, beta_y = alpha + a, beta_x + bx, beta_y + by
            terms = [L_in + alpha - beta_x, L_in + alpha - beta_y, 2 * L_in - ell[i] + alpha - beta_x - beta_y]
        else:
            terms = [L_in, 2 * L_in - ell[i]]
        if i < d:
            terms.append(L[i])
        cost = max(cost, max(terms) + repeated[i])

    slack['representation budget'] = representations - demands
    slack['syndrome coordinates left for the rest'] = rest_size
    slack['error weight left for the rest'] = rest_weight
    for i in range(d):
        slack[f'saturation of level {i}'] = D[i] - fixed[i] - L[i]
        slack[f'L_{i} >= 0'] = L[i]
    return cost + runs, [name for name, value in slack.items() if value < -TOLERANCE]


def decoder(point):
    """The decoder's tree of the point's cell: its exponent with jointtrees and with this model."""
    path = os.path.join(WITNESSES, point['tree'])
    library = Witness.load(path).evaluate().time
    with open(path) as handle:
        parameters = json.load(handle)['parameters']
    here, violated = exponent(point['q'], point['rate'], point['distance'], point['depth'], parameters)
    if violated:
        raise ValueError(f"{point['tree']}: the decoder's tree violates {violated}")
    return library, here


def forced_block_margins(point):
    """The forced block of a point: its size and its error weight divided by their lower bounds (the minimum size
    and a tenth of it).  Raises ValueError if a bound is violated."""
    block = point['parameters']['blocks'][str(point['join'])]
    minimum = point['size']
    if block['size'] < minimum - BOUND_TOLERANCE or block['weight'] < minimum / 10 - BOUND_TOLERANCE:
        raise ValueError(f"q = {point['q']}, {point['distance']} distance, forced block at join {point['join']}: "
                         f"size {block['size']:.6f} or weight {block['weight']:.6f} below the bounds {minimum} and "
                         f"{minimum / 10}")
    return block['size'] / minimum, block['weight'] / (minimum / 10)


def main():
    with open(DATA) as handle:
        points = json.load(handle)['points']
    failed = 0
    decoders = {}
    for point in points:
        if point['tree'] in decoders:
            continue
        library, here = decoder(point)
        decoders[point['tree']] = here
        failed += abs(library - here) > 1e-9
        label = f"decoder of Table 5, q = {point['q']}, {point['distance']} distance, depth {point['depth']}"
        print(f'{label:62s} jointtrees {shown(library)}, this model {shown(here)}  ({library:.9f}, {here:.9f})')
    for point in points:
        value, violated = exponent(point['q'], point['rate'], point['distance'], point['depth'],
                                   point['parameters'])
        if violated:
            raise ValueError(f'a stored end point violates {violated}')
        cell = f"q = {point['q']}, {point['distance']} distance, depth {point['depth']}"
        if point['search'] == 'free blocks':
            largest = max(block['size'] for block in point['parameters']['blocks'].values())
            label = f'free blocks, {cell}, largest block {largest:.1e} n'
            print(f'{label:62s} {shown(value)}  ({value:.9f})')
            continue
        size_margin, weight_margin = forced_block_margins(point)
        change = value - decoders[point['tree']]
        note = '  the search ended at a poor point' if point.get('search_failed') else ''
        label = f"forced block >= {point['size']} n at join {point['join']}, {cell}"
        print(f'{label:62s} change {change:+.1e}  ({value:.9f}, size {size_margin:.4f} and weight '
              f'{weight_margin:.4f} times their bounds){note}')
    sys.exit(1 if failed else 0)


if __name__ == '__main__':
    main()
