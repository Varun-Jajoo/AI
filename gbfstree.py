import heapq

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def gbfs_tree(root, goal, heuristic):
    visited = set()
    priority_queue = [(heuristic[root.value], root)]  
    path = {root.value: None}
    
    while priority_queue:
        _, current_node = heapq.heappop(priority_queue)
        
        if current_node.value == goal:
            return construct_path(path, root.value, goal)
        
        visited.add(current_node.value)
        for child in current_node.children:
            if child.value not in visited:
                heapq.heappush(priority_queue, (heuristic[child.value], child))
                path[child.value] = current_node.value
    
    return None

def construct_path(path, start, goal):
    current_node = goal
    path_sequence = []
    
    while current_node:
        path_sequence.insert(0, current_node)
        current_node = path[current_node]
    
    return path_sequence if path_sequence[0] == start else None

root = TreeNode('A')
root.children = [TreeNode('S'), TreeNode('T'), TreeNode('Z')]
root.children[0].children = [TreeNode('F'), TreeNode('O'), TreeNode('R')]
root.children[1].children = []
root.children[2].children = []
root.children[0].children[0].children = [TreeNode('B')]

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

gbfs_path = gbfs_tree(root, goal_node, heuristic)
if gbfs_path:
    print('Path:', gbfs_path)
    print(f"Goal '{goal_node}' found using GBFS.")
else:
    print(f"Goal '{goal_node}' not found using GBFS.")
