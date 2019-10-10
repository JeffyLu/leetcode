# -*- coding:utf-8 -*-


class Solution:

    def StrToInt(self, s):
        legal = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-']
        if not s or s[0] not in legal[1:]:
            return 0
        flag = 1
        base = 0
        if s[0] == '-':
            s = s[1:]
            flag = -1
        elif s[0] == '+':
            s = s[1:]
        for i in s:
            if i not in legal:
                return 0
            base = base * 10 + int(i)
        return base * flag
