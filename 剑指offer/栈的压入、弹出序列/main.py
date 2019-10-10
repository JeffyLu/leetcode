# -*- coding:utf-8 -*-


class Solution:

    def IsPopOrder(self, pushV, popV):
        stack = []
        j = 0
        for i in popV:
            if stack and stack[-1] == i:
                stack.pop()
                continue
            while j < len(pushV) and pushV[j] != i:
                stack.append(pushV[j])
                j += 1
            j += 1
        return False if stack else True
