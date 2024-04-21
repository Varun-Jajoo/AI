class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

def dfs_tree(node, goal, path=None, open_list=None, closed_list=None):
    if path is None:
        path = []
    if open_list is None:
        open_list = []
    if closed_list is None:
        closed_list = []

    open_list.append(node.value)
    path.append(node.value)

    print("Iteration", len(open_list) + len(closed_list))
    print("Current Node:", node.value)
    print("Open List:", open_list)
    print("Closed List:", closed_list)

    if node.value == goal:
        return path

    for child in node.children:
        if child.value not in path:
            new_path = dfs_tree(child, goal, path[:], open_list, closed_list)
            if new_path:
                return new_path

    open_list.remove(node.value)
    closed_list.append(node.value)

    return None

# Example tree
root = TreeNode('A')
root.children = [TreeNode('B'), TreeNode('C'), TreeNode('D')]
root.children[0].children = [TreeNode('E'), TreeNode('F')]
root.children[1].children = [TreeNode('G'), TreeNode('H')]

goal_node = input("Enter the goal node: ").strip().upper()

print("DFS Path in Tree:")
open_list = []
closed_list = []
path = dfs_tree(root, goal_node, open_list=open_list, closed_list=closed_list)
if path:
    print("Path to", goal_node, ":", ' -> '.join(path))
else:
    print("Path to", goal_node, "not found.")
