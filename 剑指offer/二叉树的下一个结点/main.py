# -*- coding:utf-8 -*-


class TreeLinkNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:

    def GetNext(self, pNode):
        if pNode.right:
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
        else:
            if pNode.next and pNode.next.left == pNode:
                pNode = pNode.next
            else:
                flag = False
                while pNode.next:
                    if pNode.next.right != pNode:
                        flag = True
                    pNode = pNode.next
                if not flag:
                    return None
        return pNode
