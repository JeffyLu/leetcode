# -*- coding:utf-8 -*-


class Solution:

    def IsContinuous(self, numbers):
        if not numbers:
            return False
        num = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        numbers = sorted([num[i] if i in num else i for i in numbers])
        ghost = 0
        while numbers[ghost] == 0:
            ghost += 1
        for i in xrange(ghost+1, len(numbers)):
            val = numbers[i] - numbers[i-1] - 1
            if ghost < 0 or val < 0:
                return False
            if val == 0:
                continue
            else:
                ghost -= val
        return False if ghost < 0 else True
