# -*- coding:utf-8 -*-


class Solution:

    def insert_idx(self, data, val):
        left = 0
        right = len(data) - 1
        while left <= right:
            mid = (right + left) // 2
            if data[mid] < val:
                left += 1
            elif data[mid] > val:
                right -= 1
            return left

    def GetNumberOfK(self, data, k):
        return self.insert_idx(data, k+0.5) - self.insert_idx(data, k-0.5)
