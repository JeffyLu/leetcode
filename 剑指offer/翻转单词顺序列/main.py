# -*- coding:utf-8 -*-


class Solution:

    def ReverseSentence(self, s):
        words = s.split(' ')
        return ' '.join(words[::-1])
