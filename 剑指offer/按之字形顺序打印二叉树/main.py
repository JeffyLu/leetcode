# -*- coding:utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def Print(self, pRoot):
        if pRoot is None:
            return []
        tmp = [pRoot]
        res = []
        reverse = False
        while tmp:
            level_nodes = tmp
            tmp = []
            vals = []
            for n in level_nodes:
                vals.append(n.val)
                if n.left is not None:
                    tmp.append(n.left)
                if n.right is not None:
                    tmp.append(n.right)
            res.append(vals[::-1] if reverse else vals)
            reverse = not reverse
        return res
