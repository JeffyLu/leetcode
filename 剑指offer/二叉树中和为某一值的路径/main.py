# -*- coding:utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        if not root:
            return []
        if root.val == expectNumber:
            return [] if root.left or root.right else [[root.val]]
        sub_exp = expectNumber - root.val
        if sub_exp > 0:
            left = self.FindPath(root.left, sub_exp)
            for l in left:
                l.insert(0, root.val)
            right = self.FindPath(root.right, sub_exp)
            for r in right:
                r.insert(0, root.val)
            left.extend(right)
            res = left
        else:
            res = []
        return res
