# -*- coding:utf-8 -*-


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def ReverseList(self, pHead):
        if not pHead:
            return None
        """
        a -> b -> c
        """
        a = pHead
        b = pHead.next
        pHead.next = None
        while b:
            c = b.next
            b.next = a
            a = b
            b = c
        return a
