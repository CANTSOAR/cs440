"""Part 6: implement landmark and custom heuristics. YOU EDIT THIS FILE.

Both heuristics must be admissible and consistent on the map being searched.
Use the provided bfs_from(problem, landmark) to build distance tables.

Available fields: problem.goal, problem.w, problem.h, problem.cache, and
problem.version. problem.passable(x, y) checks the believed map. The cache
persists across replans; the version increases when blockages are discovered.
Precomputation probes and runtime are measured for you.
"""
from __future__ import annotations

from gridworld.hlib import bfs_from, corners, h_manhattan, h_zero


def _landmarks(problem):
    """Passable corners, edge midpoints and a few interior points."""
    w, h = problem.w, problem.h
    cands = corners(problem) + [(w // 2, 0), (w // 2, h - 1),
                                (0, h // 2), (w - 1, h // 2),
                                (w // 4, h // 4), (3 * w // 4, h // 4),
                                (w // 4, 3 * h // 4), (3 * w // 4, 3 * h // 4),
                                (w // 2, h // 2)]
    return [c for c in cands if problem.passable(*c)]


def h_differential(state, problem) -> float:
    """A landmark (differential) heuristic.

    TODO (Part 6a).

    Pick a few landmarks. For each landmark ``l``, one call to ``bfs_from``
    gives ``d(l, v)`` for every cell ``v``. Then

        ``h(s) = max over landmarks l of  | d(l, s) - d(l, goal) |``

    Requirements:

      * Cache the tables in ``problem.cache`` -- the same dict reaches every
        replan of one agent. Do **not** bake the goal into a table; the goal
        moves between replans. Key on the landmarks and the version the tables
        were built at.
      * Tables built at an older belief version stay admissible, so rebuilding
        is a performance decision, not a correctness one. Rebuild when
        ``problem.version - built_at > REBUILD_EVERY``.
      * Skip any landmark whose distance to ``s`` or to ``goal`` is unknown.

    Choose and justify the number and placement of landmarks. ``corners``
    returns candidate locations, which may be blocked.
    """
    cache = problem.cache
    entry = cache.get("landmarks")
    if entry is None or problem.version - entry[0] > REBUILD_EVERY:
        tables = []
        for l in _landmarks(problem):
            t = bfs_from(problem, l)
            if t:
                tables.append(t)
        entry = (problem.version, tables)
        cache["landmarks"] = entry
    goal = problem.goal
    best = 0
    for t in entry[1]:
        ds = t.get(state)
        dg = t.get(goal)
        if ds is None or dg is None:
            continue
        v = abs(ds - dg)
        if v > best:
            best = v
    return best


def h_custom(state, problem) -> float:
    """Your best admissible heuristic.

    TODO (Part 6d). Combine heuristics while preserving admissibility and
    consistency. Evaluate both search savings and precomputation cost.
    """
    return max(h_manhattan(state, problem), h_differential(state, problem))


#: How many belief versions a landmark table may be stale before you rebuild
#: it. Part 6(c) sweeps this; the report plots the sweep.
REBUILD_EVERY = 16

#: Registry the autograder and the report iterate over.
HEURISTICS = {
    "zero": h_zero,
    "manhattan": h_manhattan,
    "differential": h_differential,
    "custom": h_custom,
}
