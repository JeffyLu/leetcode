# -*- coding:utf-8 -*-


class Solution:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, node):
        if not self.min_stack or self.min_stack[-1] > node:
            self.min_stack.append(node)
        else:
            self.min_stack.append(self.min_stack[-1])
        self.stack.append(node)

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        return self.stack[-1]

    def min(self):
        return self.min_stack[-1]
