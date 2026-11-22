"""What the comparison scripts share: rounding as the paper rounds, entropies, the error weight of decoding over F_q,
and the center count of Hirose [Hir16].  Standard library only, apart from jointtrees.

Notation of the paper: exponents are in bits per n (or per n' for a single join), h is the binary entropy, H the
entropy of a type, q the field size, R the rate, omega the relative error weight, L the size exponent of a list, u
the center size, gamma the relative distance of a nearest-neighbour join.
"""
import math

from jointtrees import Decoding, PriceFilter


def round_up(value, decimals=4):
    """An exponent as the paper prints it: rounded up."""
    return math.ceil(value * 10 ** decimals - 1e-9) / 10 ** decimals


def round_down(value, decimals=4):
    """A difference of exponents as the paper prints it: rounded down."""
    return math.floor(value * 10 ** decimals + 1e-9) / 10 ** decimals


def shown(value, decimals=4, rounding=round_up):
    """The printed form of a value: rounded as the paper rounds, with a fixed number of decimals."""
    return f'{rounding(value, decimals):.{decimals}f}'


def h(x):
    """The binary entropy in bits, h(0) = h(1) = 0."""
    if x <= 0 or x >= 1:
        return 0.0
    return -x * math.log2(x) - (1 - x) * math.log2(1 - x)


def H(t):
    """The entropy in bits of a type, given as {value: share} or as a list of shares."""
    shares = t.values() if isinstance(t, dict) else t
    return -sum(x * math.log2(x) for x in shares if x > 0)


def error_weight(q, R, distance):
    """omega: the Gilbert-Varshamov weight (distance 'full') or half of it ('half'), as the library defines them."""
    return Decoding(q=q, rate=R, weight='gv' if distance == 'full' else 'gv/2').omega


def hirose_exponents(q, gamma, u, h0):
    """The center count alpha_H and the list reduction beta_H of Hirose's nearest-neighbour join [Hir16, Theorem 1],
    in bits per coordinate.  A center of Hirose is a set of u n' positions that accepts a vector whose digits on it
    have the shares h0 for the digit 0 and (1 - h0)/(q - 1) for every other digit [Hir16, Section 5].  For a pair at
    distance gamma n' of two vectors of the type (1/q, ..., 1/q), such a center contains the fraction u of every
    group of positions where the two vectors differ, and the fraction theta_i = (q h_i - gamma) u / (1 - gamma) of the
    positions where both have the digit i:

        alpha_H = (1 - gamma) (h(u) - (1/q) sum_i h(theta_i))
        beta_H  = h(u) - (1/q) sum_i h(q h_i u)

    These fractions are admissible but in general not the most frequent ones, which is why alpha_H is larger than
    the center count alpha of [neighbour join].  Returns alpha_H, beta_H and the fractions theta_i, which must lie
    in [0, 1]."""
    shares = [h0] + [(1 - h0) / (q - 1)] * (q - 1)
    theta = [(q * x - gamma) * u / (1 - gamma) for x in shares]
    alpha = (1 - gamma) * (h(u) - sum(h(t) for t in theta) / q)
    beta = h(u) - sum(h(q * x * u) for x in shares) / q
    return alpha, beta, theta


def syndrome_filter_exponents(q, J, tilt, f, size=1.0):
    """The center count alpha and the list reductions beta_x, beta_y of a syndrome filter of the paper on `size` n
    coordinates of F_q whose pairs have the joint type J = {(a, b): share}: prices z_a with all non-zero digits alike,
    `tilt` 'same' or 'own' [filter exponents].  `f` holds the filter's parameters as a witness writes them: the
    center size 'u' and the prices 'z' (and 'z_y' for the second list with its own prices)."""
    record = PriceFilter(tilt=tilt).exponents(J, f, q=q, alike=True, size=size)
    return record['alpha'], record['beta_x'], record['beta_y']
