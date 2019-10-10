# -*- coding:utf-8 -*-


class Solution:

    def replaceSpace(self, s):
        new_s = ''
        for i in s:
            if i == ' ':
                new_s += '%20'
            else:
                new_s += i
        return new_s
