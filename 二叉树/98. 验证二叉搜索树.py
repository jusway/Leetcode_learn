# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 左右中
        def dfs(node:TreeNode,min_limit,max_limit): # 返回值就是单纯的当前节点“是不是二叉搜索树”
            if node is None:
                return True

            left_is_BST=dfs(node.left,min_limit,node.val)
            right_is_BST=dfs(node.right,node.val,max_limit)

            if left_is_BST and right_is_BST and min_limit<node.val<max_limit:
                return True
            return False

        return dfs(root,float("-inf"),float("inf"))


class Solution:
    # 因为不需要左右子树的信息进行判断，所以 “中左右”
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], low_limit: float, high_limit: float) -> bool:
            if not node:
                return True

            # 信息足够，直接判断！
            if node.val <= low_limit or node.val >= high_limit:
                return False
            left_is_BST=dfs(node.left,low_limit,node.val)
            if not left_is_BST:
                return False
            right_is_BST=dfs(node.right,node.val,high_limit)
            if not right_is_BST:
                return False

            return  True

        return dfs(root, float('-inf'), float('inf'))



class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        pre = float("-inf")

        def inorder(node: Optional[TreeNode]) -> bool:
            if node is None:
                return True

            nonlocal pre

            left_is_BST=inorder(node.left)
            if not left_is_BST:
                return False

            if node.val <= pre:
                return False
            pre = node.val

            right_is_BST=inorder(node.right)
            if not right_is_BST:
                return False

            return True

        return inorder(root)



