def dfs(graph, start, goal, visited=None, path=None, open_list=None, closed_list=None):
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

    for neighbor in graph[start]:
        if neighbor not in visited:
            new_path = dfs(graph, neighbor, goal, visited, path, open_list, closed_list)
            if new_path:
                return new_path

    open_list.remove(start)
    closed_list.append(start)

    return None

#FOR GRAPH
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

print("DFS Path:")
if start_node not in graph or goal_node not in graph:
    print("Start node or goal node not found in the graph.")
else:
    open_list = []
    closed_list = []
    path = dfs(graph, start_node, goal_node, open_list=open_list, closed_list=closed_list)
    if path:
        print("Path from", start_node, "to", goal_node, ":", ' -> '.join(path))
    else:
        print("Path from", start_node, "to", goal_node, "not found.")
    print("Open List after DFS:", open_list)
    print("Closed List after DFS:", closed_list)
