# -*- coding:utf-8 -*-


class MergeSort:

    def _merge(self, arr1, arr2):
        arr = []
        while len(arr1) != 0 and len(arr2) != 0:
            if arr1[0] > arr2[0]:
                arr.append(arr2.pop(0))
            else:
                arr.append(arr1.pop(0))
        if len(arr1) == 0:
            arr.extend(arr2)
        else:
            arr.extend(arr1)
        return arr

    def _sort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            mid = len(arr) // 2
            arr1 = self._sort(arr[:mid])
            arr2 = self._sort(arr[mid:])
            return self._merge(arr1, arr2)

    def __call__(self, arr):
        return self._sort(arr)


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [i for i in arr if i < pivot]
    mid = [i for i in arr if i == pivot]
    right = [i for i in arr if i > pivot]
    return quick_sort(left) + mid + quick_sort(right)


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


class Solution:

    def GetLeastNumbers_Solution(self, tinput, k):
        if k > len(tinput):
            return []
        return bubble_sort(tinput)[:k]
