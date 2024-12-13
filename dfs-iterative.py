class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.value})"


def dfs_preorder_iterative(root):
    if not root:
        return []
    result = []
    stack = [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.right:  # Push right first so left is processed first
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return result


def dfs_inorder_iterative(root):
    result, stack = [], []
    current = root
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        result.append(current.value)
        current = current.right
    return result


def dfs_postorder_iterative(root):
    if not root:
        return []
    result, stack = [], [root]
    while stack:
        node = stack.pop()
        result.append(node.value)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]  # Reverse the result for post-order


if __name__ == "__main__":
    root = Node(2, Node(1, Node(6), Node(10)), Node(3))
    print("Pre-order:", dfs_preorder_iterative(root))  # Output: [2, 1, 6, 10, 3]
    print("In-order:", dfs_inorder_iterative(root))  # Output: [6, 1, 10, 2, 3]
    print("Post-order:", dfs_postorder_iterative(root))  # Output: [6, 10, 1, 3, 2]
