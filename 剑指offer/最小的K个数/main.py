# -*- coding:utf-8 -*-


class Solution:

    def _heapify(self, arr, length, last):
        smallest = last
        left = last * 2 + 1
        right = last * 2 + 2
        if left < length and arr[left] < arr[smallest]:
            smallest = left
        if right < length and arr[right] < arr[smallest]:
            smallest = right
        if smallest != last:
            arr[smallest], arr[last] = arr[last], arr[smallest]
            self._heapify(arr, length, smallest)

    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput) or k == 0:
            return []
        length = len(tinput)
        for i in range(int(length/2)-1, -1, -1):
            self._heapify(tinput, length, i)
        for i in range(length-1, length-1-k, -1):
            tinput[0], tinput[i] = tinput[i], tinput[0]
            self._heapify(tinput, i, 0)
        return tinput[-k:]
