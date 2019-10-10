# -*- coding:utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def Convert(self, pRootOfTree):
        stack = []
        root = None
        pre_node = None
        while pRootOfTree or stack:
            while pRootOfTree:
                stack.append(pRootOfTree)
                pRootOfTree = pRootOfTree.left
            pRootOfTree = stack.pop()
            if not root:
                root = pRootOfTree
            else:
                pre_node.right = pRootOfTree
                pRootOfTree.left = pre_node
            pre_node = pRootOfTree
            pRootOfTree = pRootOfTree.right
        return root
