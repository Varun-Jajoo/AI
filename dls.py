def dls(graph, start, goal, max_depth, depth=0, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path = path + [start]

    if start == goal:
        return path

    if depth >= max_depth:
        return None

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dls(graph, neighbor, goal, max_depth, depth + 1, visited, path)
            if new_path:
                return new_path

    return None

# Example graph represented as an adjacency list
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

#FOR TREE
graph = {
    'A': ['B', 'C','D'],
    'B': ['E', 'F'],
    'C': ['G','H'],
    'D':[],
    'E':[],
    'F':[],
    'G':[],
    'H':[]
}

start_node = input("Enter the start node: ").strip().upper()
goal_node = input("Enter the goal node: ").strip().upper()
max_depth = int(input("Enter the maximum depth: ").strip())

print("DLS Path:")
if start_node not in graph or goal_node not in graph:
    print("Start node or goal node not found in the graph.")
else:
    path = dls(graph, start_node, goal_node, max_depth)
    if path:
        print("Path from", start_node, "to", goal_node, ":", ' -> '.join(path))
    else:
        print("Path from", start_node, "to", goal_node, "not found within the maximum depth.")