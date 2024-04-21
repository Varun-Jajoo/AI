import heapq

class TreeNode:
    def __init__(self, value, cost=None):
        self.value = value
        self.cost = cost
        self.children = []

    def __repr__(self):
        return self.value

def astar_tree(root, goal, heuristic):
    visited = set()
    priority_queue = [(heuristic[root.value], 0, root)]  # Priority queue sorted by f-value (heuristic + cost)
    path_cost = {root.value: 0}
    path = {root.value: None}
    
    while priority_queue:
        print("OPEN LIST:", [(f"{heuristic[node.value] + cost}, {cost}, {node}") for _, cost, node in priority_queue])
        _, current_cost, current_node = heapq.heappop(priority_queue)
        
        if current_node.value == goal:
            return construct_path(path, root.value, goal)
        
        visited.add(current_node.value)
        for child, edge_cost in current_node.children:
            total_cost = path_cost[current_node.value] + edge_cost
            if child.value not in visited or total_cost < path_cost[child.value]:
                path_cost[child.value] = total_cost
                heapq.heappush(priority_queue, (total_cost + heuristic[child.value], total_cost, child))
                path[child.value] = current_node.value
    
    return None

def construct_path(path, start, goal):
    current_node = goal
    path_sequence = []
    while current_node:
        path_sequence.insert(0, current_node)
        current_node = path[current_node]
    return path_sequence

# Example usage
root = TreeNode('A')
root.children = [(TreeNode('B', 1), 1), (TreeNode('C', 2), 2)]
root.children[0][0].children = [(TreeNode('D', 3), 3), (TreeNode('E', 4), 4)]
root.children[1][0].children = [(TreeNode('F', 1), 1)]

start_node = input("Enter the start node: ").strip().upper()
goal_node = input("Enter the goal node: ").strip().upper()

heuristic = {
    'A': 3,
    'B': 2,
    'C': 4,
    'D': 1,
    'E': 1,
    'F': 0
}

astar_path = astar_tree(root, goal_node, heuristic)
print()
if astar_path:
    print('Path:', astar_path)
    print(f"Goal '{goal_node}' found using A*.")
else:
    print(f"Goal '{goal_node}' not found using A*.")
