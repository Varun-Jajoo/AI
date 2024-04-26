def dfs(graph, start, goal, max_depth, depth=0, visited=None, path=None, open_list=None, closed_list=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []
    if open_list is None:
        open_list = []
    if closed_list is None:
        closed_list = []

    visited.add(start)
    open_list.append(start)
    path = path + [start]

    print("Iteration", len(open_list) + len(closed_list))
    print("Current Node:", start)
    print("Open List:", open_list)
    print("Closed List:", closed_list)

    if start == goal:
        return path

    if depth >= max_depth:
        open_list.remove(start)
        closed_list.append(start)
        return None

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, max_depth, depth + 1, visited, path, open_list, closed_list)
            if new_path:
                return new_path

    open_list.remove(start)
    closed_list.append(start)

    return None

def dfid(graph, start, goal):
    depth = 0
    while True:
        open_list = []
        closed_list = []
        result = dfs(graph, start, goal, depth, open_list=open_list, closed_list=closed_list)
        if result is not None:
            return result
        depth += 1

# FOR GRAPH
# graph = {
#     'A': ['B', 'C'],
#     'B': ['D', 'E'],
#     'C': ['F'],
#     'D': [],
#     'E': ['F'],
#     'F': []
# }

# FOR TREE
graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': [],
    'E': [],
    'F': [],
    'G': [],
    'H': []
}

start_node = input("Enter the start node: ").strip().upper()
goal_node = input("Enter the goal node: ").strip().upper()

print("DFID Path:")
if start_node not in graph or goal_node not in graph:
    print("Start node or goal node not found in the graph.")
else:
    path = dfid(graph, start_node, goal_node)
    if path:
        print("Path from", start_node, "to", goal_node, ":", ' -> '.join(path))
    else:
        print("Path from", start_node, "to", goal_node, "not found.")
