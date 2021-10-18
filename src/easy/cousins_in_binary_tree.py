"""
Url: https://leetcode.com/problems/cousins-in-binary-tree/
Author: Konstantin Albul

Given the root of a binary tree with unique values and the values
of two different nodes of the tree x and y,
return true if the nodes corresponding to the values x and y in the tree are cousins,
or false otherwise.

Two nodes of a binary tree are cousins if they have the same depth with different parents.

Note that in a binary tree, the root node is at the depth 0,
and children of each depth k node are at the depth k + 1.

Constraints:
* The number of nodes in the tree is in the range [2, 100].
* 1 <= Node.val <= 100
* Each node has a unique value.
* x != y
* x and y are exist in the tree.
"""

from typing import Optional


# Definition for a binary tree node.
# pylint: disable=too-few-public-methods
class TreeNode:
    """Tree node
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# pylint: disable=too-few-public-methods
class Solution:
    """solution
    """


    def get_tree_nodes(self, arr: dict, node: dict, parent_val: int, depth: int) -> None:
        """Recursive tree

        Parameters
        ----------
        arr : dict
            nodes array
        node : dict
            node
        parent_val : int
            parent value
        depth : int
            depth
        """

        if node is None:
            return

        self.get_tree_nodes(arr, node.left, node.val, depth + 1)
        self.get_tree_nodes(arr, node.right, node.val, depth + 1)

        arr[node.val] = {
            'parent_val': parent_val,
            'depth': depth
        }


    # pylint: disable=no-self-use
    def is_cousins(self, root: Optional[TreeNode], x_val: int, y_val: int) -> bool:
        """cousins-in-binary-tree

        Parameters
        ----------
        root : Optional[TreeNode]
            [description]
        x_val : int
            x_val node value
        y_val : int
            y_val node value

        Returns
        -------
        bool
            is nodes cousins
        """

        if root.left is None or root.right is None:
            return False

        arr = {}
        self.get_tree_nodes(arr, root, root.val, 1)

        x_parent_val = arr[x_val]['parent_val']
        x_depth = arr[x_val]['depth']

        y_parent_val = arr[y_val]['parent_val']
        y_depth = arr[y_val]['depth']

        output = False
        if x_parent_val != y_parent_val and x_depth == y_depth:
            output = True

        return output


if __name__ == "__main__":
    solution = Solution()

    # Input: root = [1,2,3,4], x = 4, y = 3
    # Output: false
    assert solution.is_cousins(
        TreeNode(1,
                 left=TreeNode(2, left=TreeNode(4), right=None),
                 right=TreeNode(3)
        ), 4, 3) is False

    # Input: root = [1,2,3,4], x = 2, y = 3
    # Output: true
    assert solution.is_cousins(
        TreeNode(1,
                 left=TreeNode(2, left=TreeNode(4), right=None),
                 right=TreeNode(3)
        ), 2, 3) is False

    # Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    # Output: true
    assert solution.is_cousins(
        TreeNode(1,
                 left=TreeNode(2, left=None, right=TreeNode(4)),
                 right=TreeNode(3, left=None, right=TreeNode(5))
        ), 5, 4) is True

    # Input: root = [1,2,3,null,4,null,5], x = 5, y = 4
    # Output: true
    assert solution.is_cousins(
        TreeNode(1,
                 left=TreeNode(2, left=None, right=TreeNode(4)),
                 right=TreeNode(3, left=None, right=TreeNode(5))
        ), 2, 5) is False

    # Input: root = [1,2,3,null,4,null,5], x = 2, y = 3
    # Output: true
    assert solution.is_cousins(
        TreeNode(1,
                 left=TreeNode(2, left=None, right=TreeNode(4)),
                 right=TreeNode(3, left=None, right=TreeNode(5))
        ), 2, 3) is False

    # Input: root = [1,2,3,null,4], x = 2, y = 3
    # Output: false
    assert solution.is_cousins(
        TreeNode(1,
                 left=TreeNode(2, left=None, right=TreeNode(4)),
                 right=TreeNode(3, left=None, right=None)
        ), 2, 3) is False
