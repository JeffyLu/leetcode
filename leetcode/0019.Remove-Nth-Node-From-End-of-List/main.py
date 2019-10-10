# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def traverse(self):
        res = [self.val]
        temp = self.next
        while temp:
            res.append(temp.val)
            temp = temp.next
        return res

    def __str__(self):
        return str(self.traverse())


class Solution:
    def removeNthFromEnd(self, head, n):
        fast = head
        slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            head = head.next
            return head
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head


if __name__ == '__main__':

    s = Solution()
    c1 = ListNode(1)
    temp = c1
    for i in [2, 3, 4, 5]:
        temp.next = ListNode(i)
        temp = temp.next
    c2 = ListNode(1)
    c2.next = ListNode(2)
    cases = [
        [c1, 2, [1, 2, 3, 5]],
        [ListNode(1), 1, []],
        [c2, 2, [2]]
    ]
    for case in cases:
        res = s.removeNthFromEnd(case[0], case[1])
        res = res.traverse() if res else []
        assert res == case[2], 'expected: {}, got: {}'.format(
            case[2], res)
