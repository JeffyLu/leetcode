# -*- coding:utf-8 -*-


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def FindFirstCommonNode(self, pHead1, pHead2):
        node1 = []
        node2 = []
        while pHead1:
            node1.append(pHead1)
            pHead1 = pHead1.next
        while pHead2:
            node2.append(pHead2)
            pHead2 = pHead2.next
        common = None
        while node1 and node2:
            n1 = node1.pop()
            n2 = node2.pop()
            if n1 == n2:
                common = n1
        return common
