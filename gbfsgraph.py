import heapq

def gbfs(graph, start, goal, heuristic):
    visited = set()
    priority_queue = [(heuristic[start], start)]  
    path = {start: None}
    
    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)
        
        if current_node == goal:
            return construct_path(path, start, goal)
        
        visited.add(current_node)
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (heuristic[neighbor], neighbor))
                path[neighbor] = current_node
    
    return None

def construct_path(path, start, goal):
    current_node = goal
    path_sequence = []
    
    while current_node:
        path_sequence.insert(0, current_node)
        current_node = path[current_node]
    
    return path_sequence if path_sequence[0] == start else None

graph = {
    'A': ['S', 'T', 'Z'],
    'S': ['A', 'F', 'O', 'R'],
    'T': [],
    'Z': [],
    'F': ['S', 'B']
}

start_node = input("Enter the start node: ").strip().upper()
goal_node = input("Enter the goal node: ").strip().upper()

heuristic = {
    'A': 366,
    'S': 253,
    'F': 176,
    'T': 329,
    'O': 380,
    'Z': 374,
    'R': 193,
    'B': 0
}

gbfs_path = gbfs(graph, start_node, goal_node, heuristic)
if gbfs_path:
    print('Path:', gbfs_path)
    print(f"Goal '{goal_node}' found using GBFS.")
else:
    print(f"Goal '{goal_node}' not found using GBFS.")
