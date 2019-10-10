# -*- coding:utf-8 -*-


class Solution:

    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return 0
        left = 0
        right = len(rotateArray) - 1
        mid = 0
        while rotateArray[left] >= rotateArray[right]:
            if left + 1 == right:
                mid = right
                break
            mid = (left + right) / 2
            if rotateArray[left] == rotateArray[right] and rotateArray[left] == rotateArray[mid]:
                return min(rotateArray[left:right+1])
            if rotateArray[mid] >= rotateArray[left]:
                left = mid
            else:
                right = mid
        return rotateArray[mid]
