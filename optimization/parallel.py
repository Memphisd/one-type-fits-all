"""Independent searches in parallel processes, each with a time limit (inventory: strategies 18, 20, 21, 27).

    python3 optimization/parallel.py                the example below (subset sum, 8 seeds in 4 processes, ~3 minutes)

Each process runs `optimize` with its own seed and a wall-clock limit and returns a witness (plain data, so that it
can cross the process boundary), and the best is kept.  The per-start reports of every run (result.starts) show which
starts were cut by the time limit.
"""
from concurrent.futures import ProcessPoolExecutor

from common import run, say
from jointtrees import SubsetSum, Witness, filtered


def one_search(job):
    problem, tree, seed, starts, limit = job
    result = run(problem, tree, seed=seed, starts=starts, time_limit=limit)
    if result is None:
        return seed, None, []
    return seed, result.witness(seed=seed).to_dict(), result.starts


def parallel(problem, tree, seeds, starts=4, limit=60, processes=4, log=None):
    """The best witness over independent searches with the given seeds."""
    jobs = [(problem, tree, seed, starts, limit) for seed in seeds]
    found = []
    with ProcessPoolExecutor(processes) as pool:
        for seed, data, starts_report in pool.map(one_search, jobs):
            cut = sum(s['status'] == 'cut' for s in starts_report)
            found_time = 'no feasible point' if data is None else f"{data['claimed']['time']:.9f}"
            say(f'seed {seed}: {found_time}  ({cut} starts cut)', log)
            if data is not None:
                found.append(Witness.from_dict(data))
    return min(found, key=lambda w: w.claimed['time']) if found else None


if __name__ == '__main__':
    best = parallel(SubsetSum(), filtered(depth=3, digits=(-1, 0, 1)), seeds=range(1, 9), starts=3, limit=90)
    print(f'best: {best.claimed["time"]:.6f}')
