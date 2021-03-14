from collections import deque


class TreeNode:
    # Definition for a binary tree node.
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def invert_tree(root: TreeNode) -> TreeNode:
    """
    Inverting the btree via recursion
    :param: root of binary tree:
    :returns: inverted binary tree
    """
    if root is None:
        return 0
    root.left, root.right = root.right, root.left
    if root.left:
        invert_tree(root.left)
    if root.right:
        invert_tree(root.right)
    return root


def max_level_sum(root: TreeNode) -> int:
    """
    return s maximum sum of a level in Binary Tree
    param: root of the btree
    returns max sum of level
    """
    if root is None:
        return 0

    result = root.data

    q = deque()
    q.append(root)

    while len(q) > 0:

        count = len(q)

        summary = 0
        while count > 0:
            temp = q.popleft()
            summary += temp.data
            if temp.left is not None:
                q.append(temp.left)
            if temp.right is not None:
                q.append(temp.right)
            count -= 1
        result = max(summary, result)

    return result


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(8)
    root.right.right.left = TreeNode(6)
    root.right.right.right = TreeNode(7)

    #              1
    #            /   \
    #          2      3
    #        /  \      \
    #       4    5      8
    #     /   \
    #    7     6
    print(max_level_sum(root))  # 17
    inverted_root = (invert_tree(root))
    print(inverted_root.right.left.data, inverted_root.right.right.data) # 5 4
