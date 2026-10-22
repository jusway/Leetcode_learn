from functools import cache


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode | None) -> int:

        @cache
        def f(node: TreeNode): # 以node为根的子树 最高金额
            if node is None:
                return 0

            # 不选当前 node
            skip = f(node.left)+f(node.right)
            # 选当前 node
            steal= node.val
            if node.left:
                steal+=f(node.left.left) + f(node.left.right)

            if node.right:
                steal += f(node.right.left) + f(node.right.right)

            return max(skip,steal)

        return f(root)


class Solution:
    def rob(self, root: TreeNode | None) -> int:

        def dfs(node: TreeNode): # (以node为根的子树 在不选node时候的 最高能偷的金额 , 以node为根的子树 在选node时候的 最高能偷的金额)
            if node is None:
                return (0,0)

            left_skip,left_steal=dfs(node.left)
            right_skip,right_steal=dfs(node.right)

            # 不选当前 node
            skip = max(left_skip,left_steal)+max(right_skip,right_steal)
            # 选当前 node
            steal = node.val+left_skip+right_skip

            return (skip,steal)

        skip, steal=dfs(root)
        return max(skip,steal)















