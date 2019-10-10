# -*- coding:utf-8 -*-


class RandomListNode:

    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:

    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return None
        p = pHead
        while p:
            node = RandomListNode(p.label)
            node.next = p.next
            p.next = node
            p = p.next.next
        p = pHead
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        new_head = pHead.next
        p = new_head
        h = pHead
        while p.next:
            h.next = p.next
            h = h.next
            p.next = p.next.next
            p = p.next
        h.next = None
        return new_head
