# -*- coding:utf-8 -*-


class Solution:

    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        res = set()
        for i in array:
            if i in res:
                res.remove(i)
            else:
                res.add(i)
        return list(res)
