from collections import deque
def bfs(graph, start, goal):
    queue = deque([start])
    visited = {start: None}

    while queue:
        node = queue.popleft()
        if node == goal:
            return construct_path(visited, start, goal)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited[neighbor] = node
                queue.append(neighbor)
    return None

def construct_path(visited, start, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = visited[goal]
    return list(reversed(path))
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = input("Enter the start node: ").strip().upper()
goal_node = input("Enter the goal node: ").strip().upper()

print("BFS Path:")
if start_node not in graph or goal_node not in graph:
    print("Start node or goal node not found in the graph.")
else:
    path = bfs(graph, start_node, goal_node)
    if path:
        print("Path from", start_node, "to", goal_node, ":", ' -> '.join(path))
    else:
        print("Path from", start_node, "to", goal_node, "not found.")
