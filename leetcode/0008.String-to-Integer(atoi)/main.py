class Solution:

    def myAtoi(self, str):
        if not str:
            return 0
        start = 0
        length = len(str)
        while str[start] == ' ':
            start += 1
            if start == length:
                return 0
        flag = 1
        if str[start] == '-':
            flag = -1
            start += 1
        elif str[start] == '+':
            start += 1
        elif str[start] < '0' and str[start] > '9':
            return 0
        end = start
        while end < length:
            if str[end] < '0' or str[end] > '9':
                break
            end += 1
        num = int(str[start:end] or 0) * flag
        if num < -2147483648:
            return -2147483648
        elif num > 2147483647:
            return 2147483647
        else:
            return num
