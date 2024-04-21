from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def bfs_tree(root, goal):
    queue = deque([root])
    parents = {root: None}

    while queue:
        node = queue.popleft()
        if node.value == goal:
            return construct_path(parents, node)
        for child in node.children:
            if child not in parents:
                parents[child] = node
                queue.append(child)
    return None

def construct_path(parents, goal):
    path = []
    while goal is not None:
        path.append(goal.value)
        goal = parents[goal]
    return list(reversed(path))
root = TreeNode('A')
root.children = [TreeNode('B'), TreeNode('C'), TreeNode('D')]
root.children[0].children = [TreeNode('E'), TreeNode('F')]
root.children[1].children = [TreeNode('G'), TreeNode('H')]

goal_node = input("Enter the goal node: ").strip().upper()

print("BFS Path in Tree:")
path = bfs_tree(root, goal_node)
if path:
    print("Path to", goal_node, ":", ' -> '.join(path))
else:
    print("Path to", goal_node, "not found.")
