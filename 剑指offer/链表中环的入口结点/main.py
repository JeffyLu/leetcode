# -*- coding:utf-8 -*-


class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def EntryNodeOfLoop(self, pHead):
        dup = set()
        while pHead and pHead not in dup:
            dup.add(pHead)
            pHead = pHead.next
        return pHead
