# -*- coding:utf-8 -*-


class Solution:

    def GetNumberOfK(self, data, k):
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (right + left) // 2
            if data[mid] == k:
                break
            elif data[mid] > k:
                right = mid - 1
            else:
                left = mid + 1
        if left > right:
            return 0
        cnt = 1
        l = mid - 1
        r = mid + 1
        lend = False
        rend = False
        while True:
            if lend and rend:
                break
            if l >= 0:
                if data[l] == k:
                    cnt += 1
                else:
                    lend = True
            else:
                lend = True
            if r < len(data):
                if data[r] == k:
                    cnt += 1
                else:
                    rend = True
            else:
                rend = True
            l -= 1
            r += 1
        return cnt
