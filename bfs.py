from collections import deque
from typing import List, Optional


class Node:
    def __init__(
        self,
        value: Optional[int] = None,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
    ):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node: ({self.value})"


def BFS(root: Optional[Node]) -> List[Optional[int]]:
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()  # O(1) deque operation
        result.append(node.value)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result


#            2
#         /     \
#        1        3
#       /  \     /  \
#      6   10  20   15
#          / \
#         100 200
#         /  \
#        90   80
#       / \  / \
#      16 15 12 14
#            /  /
#           99 800
#              /
#             1000
#             /
#            12

if __name__ == "__main__":
    root = Node(
        2,
        Node(
            1,
            Node(6),
            Node(
                10,
                Node(
                    100,
                    Node(90, Node(16), Node(15)),
                    Node(80, Node(12, Node(99)), Node(14, Node(800, Node(1000)))),
                ),
                Node(200),
            ),
        ),
        Node(3),
    )
    bfs_result = BFS(root)
    print("BFS Traversal Result:", bfs_result)  # Print outside BFS for flexibility
