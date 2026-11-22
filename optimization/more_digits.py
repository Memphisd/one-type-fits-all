"""Larger digit sets for the lists (inventory: strategies 5, 24, the digit sets of the LWE and subset-sum tables).

    python3 optimization/more_digits.py             the example below (~30 minutes)

The example: LWE with a ternary key, depth 3, 0.3549 on the digits -1..1 and 0.3417 on -2..2 (rounded up).

The best tree on the digits -m..m is written for the digits -(m+1)..m+1: the new digits start at share 0 (the time
stays the same) and their prices continue the outer prices in a straight line (`with_digits`).  The search then
moves mass onto the new digits if that helps.  The chain stops when one more digit on each side gains at most EPS.
"""
from common import best, release_centers, run, say, stable
from jointtrees import LWE, evaluate, filtered
from jointtrees.starts import with_digits

EPS = 1e-4          # one more digit on each side must gain more than this


def more_digits(problem, tree_on, first, result=None, largest=6, starts=2, log=None):
    """The best result over the digit sets -m..m, m = first, first + 1, ...: tree_on(digits) is the tree on a digit
    set.  `result`: an optimum on the first set, if known."""
    digits = tuple(range(-first, first + 1))
    result = result or run(problem, tree_on(digits), starts=starts)
    say(f'digits {digits[0]}..{digits[-1]}: {result.time:.9f}', log)
    while digits[-1] < largest:
        wider = tuple(range(digits[0] - 1, digits[-1] + 2))
        tree = tree_on(wider)
        start = with_digits(result, problem, tree)
        assert abs(evaluate(problem, tree, start).time - result.time) < 1e-9      # the new digits change nothing yet
        new = run(problem, tree, warm=start, starts=starts)
        new = release_centers(stable(new)) if new is not None else None
        say(f'digits {wider[0]}..{wider[-1]}: {new.time if new else float("nan"):.9f}', log)
        if new is None or new.time > result.time - EPS:
            break
        digits, result = wider, new
    return result


if __name__ == '__main__':
    key = LWE(key={-1: 1/4, 0: 1/2, 1: 1/4})
    winner = more_digits(key, lambda digits: filtered(depth=3, digits=digits), first=1, largest=2, starts=1)
    print(f'best digits {winner.tree.digits}: {winner.time:.6f}')
