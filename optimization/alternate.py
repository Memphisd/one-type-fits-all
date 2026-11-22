"""Hold one group of variables, optimize, release it, then the next group (inventory: strategies 14, 22).

    python3 optimization/alternate.py              the example below (subset sum, depth 3, digits -1..1, ~3 minutes)

1. every filter center held at u = 0.5, optimized.  2. released.
3. the joint types of the lowest join held where step 2 left them, optimized.  4. released.
The best of the four results is returned.
"""
from common import best, run, say
from jointtrees import SubsetSum, filtered, parameter_names


def centers(problem, tree):
    """The names of all free center sizes: filter[j].u, syndrome_filter.u, parts[k].filter[j].u."""
    return [name for name in parameter_names(problem, tree) if name.endswith('.u')]


def lowest_joint_types(P):
    """{name: joint type} of every joint type of the lowest join that has one (all parts)."""
    groups = {'': P, **{f'parts[{k}].': g for k, g in P.get('parts', {}).items()}}
    found = {}
    for prefix, g in groups.items():
        for i, J in g.get('J', {}).items():
            found[i, f'{prefix}J[{i}]'] = J
    low = min(i for i, _ in found)
    return {name: J for (i, name), J in found.items() if i == low}


def alternate(problem, tree, memory_bound=None, starts=4, warm=None, log=None, **options):
    held = run(problem, tree, memory_bound=memory_bound, starts=starts, warm=warm,
               fixed={name: 0.5 for name in centers(problem, tree)}, **options)
    if held is None:
        say('centers at 0.5: no feasible point', log)
        return None
    released = run(problem, tree, memory_bound=memory_bound, starts=0, warm=held, **options)
    say(f'centers held at 0.5: {held.time:.9f}, released: {released.time if released else None}', log)
    top = best(held, released)
    fixed = lowest_joint_types(top.parameters)
    held_J = run(problem, tree, memory_bound=memory_bound, starts=0, warm=top, fixed=fixed, **options)
    released_J = run(problem, tree, memory_bound=memory_bound, starts=0, warm=held_J, **options) if held_J else None
    say(f'{", ".join(fixed)} held: {held_J.time if held_J else None}, released: '
        f'{released_J.time if released_J else None}', log)
    return best(held, released, held_J, released_J)


if __name__ == '__main__':
    winner = alternate(SubsetSum(), filtered(depth=3, digits=(-1, 0, 1)), starts=3, time_limit=45)
    print(f'best: {winner.time:.9f}')
