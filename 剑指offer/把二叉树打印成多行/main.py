# -*- coding:utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        nodes = [pRoot]
        res = []
        while nodes:
            tmp = nodes
            nodes = []
            level_val = []
            for t in tmp:
                if not t:
                    continue
                level_val.append(t.val)
                nodes.append(t.left)
                nodes.append(t.right)
            if level_val:
                res.append(level_val)
        return res
