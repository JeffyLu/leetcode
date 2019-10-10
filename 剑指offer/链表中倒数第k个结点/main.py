# -*- coding:utf-8 -*-


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def FindKthToTail(self, head, k):
        if head is None or k < 1:
            return None
        pre = head
        last = head
        for i in xrange(k-1):
            last = last.next
            if last is None:
                return None
        while last.next is not None:
            pre = pre.next
            last = last.next
        return pre
