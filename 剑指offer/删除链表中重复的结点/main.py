# -*- coding:utf-8 -*-


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteDuplication(self, pHead):
        nodes = []
        while pHead:
            if not nodes or nodes[-1].val != pHead.val:
                nodes.append(pHead)
                pHead = pHead.next
            else:
                val = nodes.pop().val
                while pHead and pHead.val == val:
                    pHead = pHead.next
        for i in xrange(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        if nodes:
            nodes[-1].next = None
            return nodes[0]
        else:
            return None
