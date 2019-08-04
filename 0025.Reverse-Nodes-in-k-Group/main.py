class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def traverse(self):
        head = self
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    @staticmethod
    def build(*arr):
        node = None
        head = None
        for i in arr:
            tmp = ListNode(i)
            if node:
                node.next = tmp
                node = node.next
                continue
            node = tmp
            head = tmp
        return head


class Solution:

    def reverseKGroup(self, head, k):
        if k <= 1 or head is None or head.next is None:
            return head

        node = head
        last = None
        while node:
            forward = node.next
            for i in range(k-1):
                if not forward:
                    return head
                forward = forward.next

            tmp_last = node
            tmp = node.next
            node.next = last
            tmp_head = node
            for i in range(k-1):
                node = tmp
                tmp = node.next
                node.next = tmp_head
                tmp_head = node
            node = tmp

            if last:
                last.next = tmp_head
            else:
                head = tmp_head
            last = tmp_last
            last.next = node
        return head


if __name__ == '__main__':

    s = Solution()
    cases = [
        [None, 5, []],
        [ListNode.build(1), 1, [1]],
        [ListNode.build(1, 2), 2, [2, 1]],
        [ListNode.build(1, 2, 3, 4), 2, [2, 1, 4, 3]],
        [ListNode.build(1, 2, 3, 4), 3, [3, 2, 1, 4]],
        [ListNode.build(1, 2, 3, 4, 5), 2, [2, 1, 4, 3, 5]],
        [ListNode.build(1, 2, 3, 4, 5), 3, [3, 2, 1, 4, 5]],
        [ListNode.build(1, 2, 3, 4, 5, 6), 3, [3, 2, 1, 6, 5, 4]],
    ]
    for c in cases:
        res = s.reverseKGroup(c[0], c[1])
        res = [] if not res else res.traverse()
        assert res == c[2], 'expected: {}, got: {}'.format(c[2], res)
