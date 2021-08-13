from chromatic_number import chromatic_number
from graph import input_graph, induced_subgraph, colorings, is_valid_coloring, remap

print('Enter number of colors, q: ', end='')
q = int(input())
print('Please note that q isn\'t part of the input.')
print(f'\n...Commencing {q}-coloring algorithm...\n')

graph = input_graph()
N = len(graph)
print('Enter vertex cover as space seperated numbers: ')
vertex_cover = [int(v) for v in input().split(' ')]
print('\nPlease note that vertex cover is not part of the input.\n'
    'Rather, it is taken as input as a matter of convenience\n')

vc_induced_subgraph = induced_subgraph(graph, vertex_cover)
X = chromatic_number(remap(vc_induced_subgraph))
print(f'Chromatic Number of the subgraph induced by Vertex Cover = {X}')

if X < q:
    print('YES')
elif X > q:
    print('NO')
else:
    q_coloring = [0]*N
    for color_map in colorings(vertex_cover, q):
        coloring_possible = True
        if is_valid_coloring(vc_induced_subgraph, color_map):

            # Try to extend the coloring to the whole graph.
            for v, color in color_map.items():
                q_coloring[v] = color

            for v1 in graph.keys():
                if v1 not in vertex_cover:
                    colors = {color_map[v2] for v2 in graph[v1]}
                    if len(set(range(1, q+1)) - colors) != 0:
                        q_coloring[v1] = (set(range(1, q+1)) - colors).pop()
                    else:
                        coloring_possible = False
                        break
            
            if coloring_possible:
                print('YES')
                print(f'A {q}-coloring is: \n{q_coloring}')
                exit(0)
    
    print('NO')

