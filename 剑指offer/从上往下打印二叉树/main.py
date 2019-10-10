# -*- coding:utf-8 -*-


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        q = [root]
        res = []
        while q:
            node = q.pop(0)
            if node:
                res.append(node.val)
                q.append(node.left)
                q.append(node.right)
        return res
