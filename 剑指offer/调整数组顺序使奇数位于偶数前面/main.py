# -*- coding:utf-8 -*-


class Solution:

    def reOrderArray(self, array):
        ji = []
        ou = []
        for i in array:
            if i % 2 == 0:
                ou.append(i)
            else:
                ji.append(i)
        return ji + ou
