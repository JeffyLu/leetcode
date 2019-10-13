import random


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        _min = i
        for j in range(i+1, len(arr)):
            if arr[_min] > arr[j]:
                _min = j
        if _min != i:
            arr[_min], arr[i] = arr[i], arr[_min]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr = arr[i]
        for j in range(i-1, -1, -1):
            if arr[j] > curr:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break
    return arr


def shell_sort(arr):
    gap = len(arr) // 2
    while gap > 0:
        for i in range(gap, len(arr)):
            curr = arr[i]
            j = i
            while j >= gap and arr[j-gap] > curr:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = curr
        gap //= 2
    return arr


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    mid = []
    right = []
    for i in arr:
        if i < pivot:
            left.append(i)
        elif i > pivot:
            right.append(i)
        else:
            mid.append(i)
    return quick_sort(left) + mid + quick_sort(right)


class MergeSort:

    def _merge(self, arr1, arr2):
        arr = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] > arr2[j]:
                arr.append(arr2[j])
                j += 1
            else:
                arr.append(arr1[i])
                i += 1
        if i >= len(arr1):
            arr.extend(arr2[j:])
        else:
            arr.extend(arr1[i:])
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


if __name__ == '__main__':

    arrs = [[random.randint(0, 100) for i in range(10)]for i in range(1)]
    for arr in arrs:
        print('            in:', arr)
        print('           out:', sorted(arr[:]))

        print('   bubble sort:', bubble_sort(arr[:]))
        print('selection sort:', selection_sort(arr[:]))
        print('insertion sort:', insertion_sort(arr[:]))
        print('    shell sort:', shell_sort(arr[:]))
        print('    quick sort:', quick_sort(arr[:]))
        print('    merge sort:', MergeSort()(arr[:]))
        sorted_arr = sorted(arr)
        assert insertion_sort(arr[:]) == sorted_arr
        assert quick_sort(arr[:]) == sorted_arr
        assert MergeSort()(arr[:]) == sorted_arr
