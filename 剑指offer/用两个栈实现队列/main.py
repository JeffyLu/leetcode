# -*- coding:utf-8 -*-


class Solution:

    def __init__(self):
        self.sin = []
        self.sout = []

    def push(self, node):
        self.sin.append(node)

    def pop(self):
        if not self.sout:
            for i in xrange(len(self.sin)-1, 0, -1):
                self.sout.append(self.sin[i])
            res = self.sin[0]
            self.sin = []
            return res
        res = self.sout[-1]
        self.sout = self.sout[:-1]
        return res
