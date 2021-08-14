from typing import Dict, List
AdjacencyList = Dict[int, List[int]]
ColorMap = Dict[int, int]


def input_graph():
    """Takes graph input in adjacency list form.
    Returns the graph as an adjacency list.
    """

    print('Enter the number of vertices: ', end='')
    N = int(input())

    print('Enter vertices in adjacency list form.\n'
        'Make sure vertex numbers start from 0.')
    graph = {}
    for _ in range(N):
        line_list = [int(c) for c in input().split(' ')]
        graph[line_list[0]] = line_list[1:]

    return graph


def singleton_subsets(graph: AdjacencyList):
    """Iterates over all the singleton subsets of graph.

    The subsets are in binary repersentation with bits set in the positions corresponding to vertices in the subset.
    """

    N = len(graph)
    subset = 1
    for _ in range(N):
        yield subset<<1


def induced_subgraph(graph: AdjacencyList, vertex_subset: 'list[int]') -> AdjacencyList:
    """Returns the subgraph induced by vertex_subset.

    Keep in mind that the labels may not start from 0 in the returned subgraph.
    """

    subgraph = {}
    for v1 in vertex_subset:
        subgraph[v1] = [v2 for v2 in graph[v1] if v2 in vertex_subset]
    
    return subgraph


def colorings(vertex_subset: 'list[int]', q):
    """Iterates over all the q-colorings possible for vertex_subset.
    
    Iterator returns a dictionary with vertices as keys, and colors as values.
    Colors are represented as numbers from 1 to q.
    """

    if len(vertex_subset) == 1:
        for i in range(1, q+1):
            yield {vertex_subset[0]: i}
    else:
        for i in range(1, q+1):
            for c in colorings(vertex_subset[1:], q):
                yield {vertex_subset[0]: i, **c}


def is_valid_coloring(graph: AdjacencyList, coloring: ColorMap):
    """Checks if a coloring is proper."""
    
    for v1, Nv in graph.items():
        for v2 in Nv:
            if coloring[v1] == coloring[v2]:
                return False
    return True


def remap(graph: AdjacencyList) -> AdjacencyList:
    """Returns a graph with vertex labels remapped to start from 0.
    
    This is needed for chromatic_number to work correctly.
    """

    N = len(graph)
    remapped_graph = {}
    vertices = list(graph.keys())

    mapping = {}
    for new, old in enumerate(vertices):
        mapping[old] = new

    for v in range(N):
        remapped_graph[v] = graph[vertices[v]][:]

    for v1, Nv in remapped_graph.items():
        for index in range(len(Nv)):
            Nv[index] = mapping[Nv[index]]

    return remapped_graph
