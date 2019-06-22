class Solution:

    def convert(self, s, numRows):
        if numRows == 1:
            return s
        res = [[] for _ in range(numRows)]
        index = 0
        gap = 1
        for i in s:
            res[index].append(i)
            if index == numRows - 1:
                gap = -1
            elif index == 0:
                gap = 1
            index += gap
        return ''.join(''.join(line) for line in res)
