# -*- coding:utf-8 -*-


class Solution:

    def LeftRotateString(self, s, n):
        if len(s) <= 1:
            return s
        return s[n:] + s[:n]
