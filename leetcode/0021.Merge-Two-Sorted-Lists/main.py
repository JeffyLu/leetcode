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


class Solution:

    def mergeTwoLists(self, l1, l2):
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


def node_builder(arr):
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


if __name__ == '__main__':

    s = Solution()
    cases = [
        [node_builder([1, 2, 4]), node_builder([1, 3, 4]), [1, 1, 2, 3, 4, 4]],
        [node_builder([1, 2, 3]), node_builder([]), [1, 2, 3]],
        [node_builder([1]), node_builder([1]), [1, 1]],
        [node_builder([1, 5]), node_builder([10]), [1, 5, 10]],
    ]
    for c in cases:
        res = s.mergeTwoLists(c[0], c[1]).traverse()
        assert res == c[2], 'expected: {}, got: {}'.format(c[2], res)
