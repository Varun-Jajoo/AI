class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dls_tree(node, goal, max_depth, depth=0, path=None):
    if path is None:
        path = []

    path.append(node.value)

    if node.value == goal:
        return path

    if depth >= max_depth:
        return None

    for child in node.children:
        new_path = dls_tree(child, goal, max_depth, depth + 1, path[:])
        if new_path:
            return new_path
    return None
root = TreeNode('A')
root.children = [TreeNode('B'), TreeNode('C'), TreeNode('D')]
root.children[0].children = [TreeNode('E'), TreeNode('F')]
root.children[1].children = [TreeNode('G'), TreeNode('H')]

goal_node = input("Enter the goal node: ").strip().upper()
max_depth = int(input("Enter the maximum depth: ").strip())

print("DLS Path in Tree:")
path = dls_tree(root, goal_node, max_depth)
if path:
    print("Path to", goal_node, ":", ' -> '.join(path))
else:
    print("Path to", goal_node, "not found within the maximum depth.")
