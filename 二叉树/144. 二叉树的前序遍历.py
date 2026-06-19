# Definition for a binary tree node.
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def f(node: Optional[TreeNode]):
            if node is None:
                return
            # 中
            res.append(node.val)
            # 左
            f(node.left)
            # 右
            f(node.right)

            return

        f(root)
        return res


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def f(node: Optional[TreeNode]):
            if node is None:
                return

            # 左
            f(node.left)
            # 中
            res.append(node.val)
            # 右
            f(node.right)

            return

        f(root)
        return res


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def f(node: Optional[TreeNode]):
            if node is None:
                return

            # 左
            f(node.left)
            # 右
            f(node.right)
            # 中
            res.append(node.val)

            return

        f(root)
        return res


from typing import List, Optional


class Solution:
    # 前序遍历迭代法
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)

            # 压栈逻辑
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res





