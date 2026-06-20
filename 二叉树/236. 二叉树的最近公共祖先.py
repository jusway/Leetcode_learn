# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 完备信息返回
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    # 定义返回值 (当前节点子树有 p,当前节点子树有 q,最近公共祖先 x 的地址)
    # 定义返回值 (当前节点是不是p的祖先,当前节点是不是q的祖先,最近公共祖先 x 的地址)
        def dfs(node):
            if node is None:
                return False,False,None

            left_has_p,left_has_q,left_x=dfs(node.left)
            right_has_p,right_has_q,right_x=dfs(node.right)

            cur_has_p=left_has_p or right_has_p or node==p
            cur_has_q=left_has_q or right_has_q or node==q

            cur_x=None
            if left_x:
                cur_x=left_x
            elif right_x:
                cur_x=right_x
            elif cur_has_p and cur_has_q:
                cur_x=node

            return cur_has_p,cur_has_q,cur_x

        _,_,x=dfs(root)
        return x


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 思路：如果当前节点 是 null，返回 null
        # 如果当前节点 是 p 或 q，直接返回当前节点
        # 递归查 左子树 得到 left，递归查 右子树 得到 right
        # 根据 left、right 判断：
        # left、right 都不为空 → 当前节点就是 LCA
        # 只有 left 不为空 → 答案在左子树
        # 只有 right 不为空 → 答案在右子树

        # 递归终止条件：空节点 或 找到p/q
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right













