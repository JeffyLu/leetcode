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

    def swapPairs(self, head):
        """
        1. head -> tmp ->
        2. tmp(return head) -> head(last node) -> node ->
        3. last_node -> node -> tmp ->
        """
        if head is None or head.next is None:
            return head

        tmp = head.next
        head.next = tmp.next
        tmp.next = head
        last_node = head
        node = head.next
        head = tmp

        while node and node.next:
            tmp = node.next
            node.next = tmp.next
            tmp.next = node
            if last_node is not None:
                last_node.next = tmp
            last_node = node
            node = node.next
        return head


if __name__ == '__main__':

    s = Solution()
    cases = [
        [None, []],
        [ListNode.build(1), [1]],
        [ListNode.build(1, 2), [2, 1]],
        [ListNode.build(1, 2, 3, 4), [2, 1, 4, 3]],
        [ListNode.build(1, 2, 3, 4, 5), [2, 1, 4, 3, 5]],
    ]
    for c in cases:
        res = s.swapPairs(c[0])
        res = [] if not res else res.traverse()
        assert res == c[1], 'expected: {}, got: {}'.format(c[1], res)
