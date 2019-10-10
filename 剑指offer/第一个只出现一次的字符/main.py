# -*- coding:utf-8 -*-


class Solution:

    def FirstNotRepeatingChar(self, s):
        if not s:
            return -1
        length = len(s)
        dup = set()
        for i in xrange(length):
            if s[i] in dup:
                continue
            for j in xrange(i+1, length):
                if s[i] == s[j]:
                    dup.add(s[i])
                    break
            if j == length - 1 and s[i] not in dup:
                return i
