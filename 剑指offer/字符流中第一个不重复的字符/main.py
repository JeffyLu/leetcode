# -*- coding:utf-8 -*-


class Solution:

    def __init__(self):
        self.once = []
        self.many = []

    def FirstAppearingOnce(self):
        return self.once[0] if self.once else '#'

    def Insert(self, char):
        if char in self.many:
            pass
        elif char in self.once:
            self.once.remove(char)
            self.many.append(char)
        else:
            self.once.append(char)
