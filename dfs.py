class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.value})"


def dfs_preorder(node):
    if node is None:
        return []
    return [node.value] + dfs_preorder(node.left) + dfs_preorder(node.right)


def dfs_inorder(node):
    if node is None:
        return []
    return dfs_inorder(node.left) + [node.value] + dfs_inorder(node.right)


def dfs_postorder(node):
    if node is None:
        return []
    return dfs_postorder(node.left) + dfs_postorder(node.right) + [node.value]


# visual
#      10
#    /   \
#   20     30
#         / \
#        40  50


if __name__ == "__main__":
    root = Node(2, Node(1, Node(6), Node(10)), Node(3))
    root1 = Node(10, Node(20), Node(30, Node(40), Node(50)))
    print("Pre order: ", dfs_preorder(root1))  # 10 20 30 40 50
    print("In order: ", dfs_inorder(root1))  # 20 10 40 30 50
    print("In order: ", dfs_inorder(root1))  # 20 10 40 30 50

    # print("Pre-order:", dfs_preorder(root))  # Output: [2, 1, 6, 10, 3]
    # print("In-order:", dfs_inorder(root))  # Output: [6, 1, 10, 2, 3]
    # print("Post-order:", dfs_postorder(root))  # Output: [6, 10, 1, 3, 2]
