# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # 边界条件（base case）
        if root is None:
            return 0

        # 遍历和处理
        left=self.maxDepth(root.left) # 返回左边的最大深度
        right=self.maxDepth(root.right)

        # 返回
        return  max(left,right)+1

