import pytest

from binary_tree.binary_tree import TreeNode
from binary_tree.binary_tree import TreeSolutions as ts


@pytest.fixture
def btree() -> TreeNode:
    """
    Initialize tree
    #              1
    #            /   \
    #          2      3
    #        /  \      \
    #       4    5      8
    #     /   \
    #    7     6
    @return:
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(8)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(6)
    return root


def test_level_sum(btree):
    level_sum = ts.max_level_sum(btree)
    assert level_sum == 17


def test_inversion(btree):
    inverted_root = ts.invert_tree(btree)
    assert inverted_root.left.data == 3


if __name__ == '__main__':
    test_inversion(btree)
