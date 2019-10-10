# -*- coding:utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def HasSubtree(self, pRoot1, pRoot2):
        if not all([pRoot1, pRoot2]):
            return False
        if pRoot1.val == pRoot2.val:
            res = self.is_sub_tree(pRoot1, pRoot2)
        else:
            res = False
        if res:
            return True
        else:
            return self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)

    def is_sub_tree(self, p1, p2):
        if not p2:
            return True
        elif not p1:
            return False
        if p1.val == p2.val:
            return self.is_sub_tree(p1.left, p2.left) and self.is_sub_tree(p1.right, p2.right)
        else:
            return False
