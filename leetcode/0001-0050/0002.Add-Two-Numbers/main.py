# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:

    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        p = l1
        q = l2
        curr = head
        extra = 0
        while p and q:
            res = p.val + q.val + extra
            extra = res // 10
            curr.next = ListNode(res % 10)
            curr = curr.next
            p = p.next
            q = q.next
        while p:
            res = p.val + extra
            extra = res // 10
            curr.next = ListNode(res % 10)
            curr = curr.next
            p = p.next
        while q:
            res = q.val + extra
            extra = res // 10
            curr.next = ListNode(res % 10)
            curr = curr.next
            q = q.next
        if extra:
            curr.next = ListNode(extra)
        return head.next
