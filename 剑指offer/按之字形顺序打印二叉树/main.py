# -*- coding:utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def Print(self, pRoot):
        nodes = [pRoot]
        reverse = False
        res = []
        while nodes:
            tmp = nodes
            nodes = []
            for i in tmp:
                if not i:
                    continue
                nodes.append(i.left)
                nodes.append(i.right)
            tmp = [t.val for t in tmp if t]
            if not tmp:
                break
            if reverse:
                res.append(list(reversed(tmp)))
            else:
                res.append(tmp)
            reverse = not reverse
        return res
