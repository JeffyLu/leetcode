# -*- coding:utf-8 -*-


class Solution:

    def Permutation(self, ss):
        if not ss:
            return []
        from itertools import permutations
        return list(sorted(set(''.join(i) for i in permutations(ss))))
