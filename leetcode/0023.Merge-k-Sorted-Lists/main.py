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

    def mergeKLists(self, lists):
        length = len(lists)
        if length == 0:
            return None
        elif length == 1:
            return lists[0]
        elif length > 2:
            left = self.mergeKLists(lists[:length//2])
            right = self.mergeKLists(lists[length//2:])
            return self.merge(left, right)
        return self.merge(*lists)

    def merge(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l2.val < l1.val:
            l1, l2 = l2, l1
        head = l1
        while l2:
            while l1.next and l1.next.val < l2.val:
                l1 = l1.next
            tmp = l1.next
            l1.next = l2
            l2 = l2.next
            l1.next.next = tmp
        return head


if __name__ == '__main__':

    s = Solution()
    cases = [
        [
            [
                ListNode.build(1, 4, 5),
                ListNode.build(1, 3, 4),
                ListNode.build(2, 6),
            ],
            [1, 1, 2, 3, 4, 4, 5, 6],
        ],
        [
            [
                ListNode.build(1, 4, 5),
                ListNode.build(2, 6),
            ],
            [1, 2, 4, 5, 6],
        ],
        [
            [
                ListNode.build(1, 4, 5),
            ],
            [1, 4, 5],
        ],
    ]
    for c in cases:
        res = s.mergeKLists(c[0]).traverse()
        assert res == c[1], 'expected: {}, got: {}'.format(c[1], res)
