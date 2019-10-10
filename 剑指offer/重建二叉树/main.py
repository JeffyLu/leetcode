# -*- coding:utf-8 -*-


class TreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        if not pre:
            return None
        root = TreeNode(pre[0])
        root_index = tin.index(root.val)
        root.left = self.reConstructBinaryTree(
            pre[1:root_index+1], tin[:root_index])
        root.right = self.reConstructBinaryTree(
            pre[root_index+1:], tin[root_index+1:])
        return root
