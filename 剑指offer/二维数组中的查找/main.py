# -*- coding:utf-8 -*-


class Solution:

    def Find(self, target, array):
        len_ = len(array[0]) - 1
        i = 0
        j = len_
        while i <= len_ and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                i += 1
            else:
                j -= 1
        return False
