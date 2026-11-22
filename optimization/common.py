"""Small helpers shared by the strategy scripts: logging, saving without overwriting, the best stored witness, and
the two steps most strategies repeat (restart until stable, centers held small then released)."""
import os
import time

from jointtrees import NoFeasiblePoint, Witness, optimize, polish, witness_files


def say(text, log=None):
    """Print a line with the time of day, and append it to the file `log` if given."""
    line = f'{time.strftime("%H:%M:%S")}  {text}'
    print(line, flush=True)
    if log:
        with open(log, 'a') as handle:
            handle.write(line + '\n')


def fresh(path):
    """`path`, or path_2, path_3, ... if it exists: results are never overwritten."""
    base, ext = os.path.splitext(path)
    k = 2
    while os.path.exists(path):
        path, k = f'{base}_{k}{ext}', k + 1
    return path


def best(*results):
    """The result with the lowest time (None entries are skipped)."""
    results = [r for r in results if r is not None]
    return min(results, key=lambda r: r.time) if results else None


def run(problem, tree, **options):
    """optimize, quiet, returning None instead of raising when no start is feasible."""
    try:
        return optimize(problem, tree, quiet=True, **options)
    except NoFeasiblePoint:
        return None


def best_witness(folder, problem, tree, memory_bound=None):
    """The stored witness of `problem` and `tree` (and the memory bound) with the lowest claimed time in `folder`, or
    None.  Trees are compared as the library completes them (digits, digit rule)."""
    wanted = Witness(problem, tree, memory_bound).instance.tree
    found = []
    for path in witness_files(folder) if os.path.exists(folder) else []:
        try:
            w = Witness.load(path)
        except (ValueError, KeyError):
            continue
        if w.problem == problem and w.memory_bound == memory_bound and w.instance.tree == wanted and w.claimed:
            found.append(w)
    return min(found, key=lambda w: w.claimed['time']) if found else None


def filtered_joins(tree):
    """The joins whose filter has a free center size."""
    return [i for i, join in enumerate(tree.joins) if join.filter is not None and join.filter.u == 'free']


def release_centers(result, sizes=(0.02, 0.1), joins=None, **options):
    """Strategy 15 of the inventory: the local search does not leave a center of size 1/2 by itself.  For every
    filtered join in turn, hold its center (in every part) at a small size, optimize, then let it go again, and keep
    what is better."""
    tree = result.tree
    keep = {'fixed': result.fixed, 'bounds': {k: tuple(v) for k, v in (result.bounds or {}).items()} or None}
    for j in filtered_joins(tree) if joins is None else joins:
        if tree.parts > 1:
            names = [f'parts[{k}].filter[{j}].u' for k in range(1, tree.parts + 1)]
        else:
            names = [f'filter[{j}].u']
        if any(name in (result.fixed or {}) for name in names):
            continue                                    # a center the caller fixed stays fixed
        for u in sizes:
            held = run(result.problem, tree, memory_bound=result.memory_bound, starts=0, warm=result,
                       fixed={**(result.fixed or {}), **{name: u for name in names}}, bounds=keep['bounds'], **options)
            if held is None:
                continue
            released = run(result.problem, tree, memory_bound=result.memory_bound, starts=0, warm=held, **keep,
                           **options)
            result = best(result, released)
    return result


def stable(result, **options):
    """Strategy 22: restart from the optimum until a round gains less than 1e-6 (at most 4 rounds)."""
    return polish(result, gain=1e-6, rounds=4, **options)
