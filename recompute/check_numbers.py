"""Recompute every number of the paper from its witness with the library jointtrees and compare it with the printed
value.

    python3 recompute/check_numbers.py            (from the root of this repository)

numbers.csv, next to this script, has one row per printed number: where it is in the paper, the printed value, the
quantity, how the paper rounds it, the witness files (paths under witnesses/, separated by semicolons) and a note.

    quantity      time          the time exponent of the tree, in bits per n
                  F             the time in base q, time / log2 q (decoding over F_q and in the Lee metric)
                  memory        the memory exponent
                  memory_bound  the memory bound M of the file
                  depth         the depth of the tree (a depth label or a column d)
                  difference    the time of the first file minus the time of each further file
                  none          nothing to compute: a count, a closed form, a claim without a number, or a number
                                that no tree of the library gives.  The note says why
                  otherwise     an expression in the values of one tree: L, D, r, c, alpha, beta_x, beta_y, ell, ell_d,
                                p, J, u (center size) and theta (center fractions) per level or join, parts[k] and
                                u_part[i][k] (center size of part k at join i) with partitioning, nonzero(type),
                                e.g. J[5][2][-1], theta[5][2, -1] or 0.3557 - time
    rounding      up, down, nearest   to the decimals of the printed value (exponents up, differences down)
                  percent       to nearest, as a percentage with the decimals of the printed value
                  exact         equal to the printed number
                  below:X       below X
                  within:X      at most X away from 0
                  none          not compared

A row with several files must hold for each of them.  The script prints one line per row and a summary, and exits
with 1 if a printed value and its witness disagree.  It evaluates every witness once and runs no search.
"""
import csv
import math
import os
import sys

from jointtrees import Witness

HERE = os.path.dirname(os.path.abspath(__file__))
WITNESSES = os.path.join(os.path.dirname(HERE), 'witnesses')


def nonzero(t):
    """The share of the non-zero digits of a type."""
    return 1 - t.get(0, 0.0)


def tree_values(path, cache):
    """The values of the evaluation of one witness under the names of numbers.csv (evaluated once)."""
    if path not in cache:
        w = Witness.load(os.path.join(WITNESSES, path))
        ev = w.evaluate()
        filters = []                                        # the filter of the tree part at every join, or None
        for join in ev.joins:
            records = [x for x in join['filters'] if x['kind'] != 'none' and x['part'] != 'rest']
            filters.append(records[0] if len(records) == 1 else None)
        names = dict(time=ev.time, F=ev.F, memory=ev.memory, memory_bound=w.memory_bound, depth=w.tree.depth,
                     L=ev.L, D=ev.D, r=ev.r, c=ev.c, alpha=ev.alpha, beta_x=ev.beta_x, beta_y=ev.beta_y, ell=ev.ell,
                     ell_d=ev.ell_d, nonzero=nonzero, u=[None if f is None else f['u'] for f in filters],
                     theta=[None if f is None else f['theta'] for f in filters])
        if w.tree.parts > 1:
            names['parts'] = ev.parts
            names['u_part'] = [{int(x['part'].split('_')[1]): x['u'] for x in join['filters']
                                if x['kind'] != 'none' and x['part'].startswith('tree_')} for join in ev.joins]
        else:
            names.update(p=ev.p, J=ev.J)
        cache[path] = names
    return cache[path]


def value_of(row, path, cache):
    """The quantity of a row for one witness."""
    names = tree_values(path, cache)
    if row['quantity'] in names:
        return names[row['quantity']]
    return eval(row['quantity'], {'__builtins__': {}}, names)          # an expression of numbers.csv


def decimals(printed):
    number = printed.rstrip('%')
    return len(number.split('.')[1]) if '.' in number else 0


def shown(value, rounding, printed):
    """The value as the paper prints it."""
    k = decimals(printed)
    if rounding == 'percent':
        value *= 100
    if rounding == 'up':
        value = math.ceil(value * 10 ** k - 1e-9) / 10 ** k
    elif rounding == 'down':
        value = math.floor(value * 10 ** k + 1e-9) / 10 ** k
    text = f'{value:.{k}f}'
    if float(text) == 0:                                    # no -0.000
        text = text.lstrip('-')
    return text + '%' if rounding == 'percent' else text


def agrees(value, rounding, printed):
    """(agrees, the value as shown)."""
    if rounding.startswith('below:'):
        return value < float(rounding[6:]), f'{value:.6g}'
    if rounding.startswith('within:'):
        return abs(value) <= float(rounding[7:]), f'{value:+.6g}'
    if rounding == 'exact':
        return value == float(printed), f'{value:g}'
    text = shown(value, rounding, printed)
    return text == printed, text


def check(row, cache):
    """(status, the computed values as text) of one row: status 'ok', 'DIFFERS' or 'not computed'."""
    if row['quantity'] == 'none':
        return 'not computed', ''
    files = row['files'].split(';')
    if row['quantity'] == 'difference':
        first, *others = (tree_values(path, cache)['time'] for path in files)
        values = [first - other for other in others]
    else:
        values = [value_of(row, path, cache) for path in files]
    results = [agrees(value, row['rounding'], row['printed']) for value in values]
    status = 'ok' if all(ok for ok, _ in results) else 'DIFFERS'
    return status, ', '.join(text for _, text in results)


def main():
    with open(os.path.join(HERE, 'numbers.csv'), newline='') as handle:
        rows = list(csv.DictReader(handle))
    cache, counts, differing = {}, {'ok': 0, 'DIFFERS': 0, 'not computed': 0}, []
    for row in rows:
        status, computed = check(row, cache)
        counts[status] += 1
        line = f"{status:12s}  {row['location']}: printed {row['printed']}"
        if computed:
            line += f', from the witness {computed}'
        if status == 'DIFFERS':
            differing.append(row)
            line += f"  ({row['note'] or row['files']})"
        print(line, flush=True)
    print(f"\n{len(rows)} printed numbers, {len(cache)} witnesses: {counts['ok']} agree, {counts['DIFFERS']} differ, "
          f"{counts['not computed']} not computed (counts, closed forms, claims, numbers of no tree of the library)")
    for row in differing:
        print(f"  DIFFERS  {row['location']}: printed {row['printed']}, {row['files']}")
    sys.exit(1 if differing else 0)


if __name__ == '__main__':
    main()
