# -*- coding:utf-8 -*-


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def Merge(self, pHead1, pHead2):
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            head = pHead1
            a = pHead1
            b = pHead2
        else:
            head = pHead2
            a = pHead2
            b = pHead1
        while b:
            while a.next and a.next.val <= b.val:
                a = a.next
            tmp = b.next
            b.next = a.next
            a.next = b
            b = tmp
        return head
