import math
from graph import singleton_subsets
from typing import Dict, List
AdjacencyList = Dict[int, List[int]]

def recursiveDP(graph: AdjacencyList):
    """Returns a Memoized closure for calculating s(X)."""

    N = len(graph)
    no_of_subsets = 2**N
    s = [-1]*no_of_subsets
    s[0] = 0
    for subset in singleton_subsets(graph):
        s[subset] = 1

    def S(X: int) -> int:
        if s[X] >= 0:
            return s[X]

        v = int(math.log(X, 2))
        bitmask = 1 << v
        X_minus_v = X ^ bitmask

        Nv = 1<<v
        for vertex in graph[v]:
            Nv |= 1<<vertex
        bitmask = (no_of_subsets-1) ^ Nv    # One's complement
        X_minus_Nv = bitmask & X

        s[X] = S(X_minus_v) + S(X_minus_Nv) + 1
        return s[X]

    return S


def no_of_covers(graph: AdjacencyList, k):
    """Returns number of ways to cover graph with k independent sets."""

    N = len(graph)
    res = 0
    s = recursiveDP(graph)
    no_of_subsets = 2**N
    for X in range(no_of_subsets):
        size = bin(X).count('1')
        res += (-1)**size * s((no_of_subsets - 1) ^ X)**k

    return res


def chromatic_number(graph: AdjacencyList):
    """Returns chromatic number of the graph."""

    N = len(graph)
    l = 1
    r = N

    while l <= r:
        if l == r:
            return l
        mid = math.floor(l + (r-l)/2)
        if no_of_covers(graph, mid) > 0:
            r = mid
        else:
            l = mid + 1
