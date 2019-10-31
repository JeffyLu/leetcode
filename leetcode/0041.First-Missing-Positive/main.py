class Solution:

    def heapify(self, arr, length, last):
        smallest = last
        left = last * 2 + 1
        right = last * 2 + 2
        if left < length and arr[left] < arr[smallest]:
            smallest = left
        if right < length and arr[right] < arr[smallest]:
            smallest = right
        if smallest != last:
            arr[smallest], arr[last] = arr[last], arr[smallest]
            self.heapify(arr, length, smallest)

    def firstMissingPositive(self, nums):
        length = len(nums)
        if length <= 1:
            return 2 if nums and nums[0] == 1 else 1
        for i in range(int(length/2)-1, -1, -1):
            self.heapify(nums, length, i)
        res = 1
        for i in range(length-1, -1, -1):
            if nums[0] > res:
                break
            elif nums[0] == res:
                res += 1
            nums[0], nums[i] = nums[i], nums[0]
            self.heapify(nums, i, 0)
        return res


if __name__ == '__main__':

    s = Solution()
    cases = [
        [[], 1],
        [[-1], 1],
        [[3], 1],
        [[1], 2],
        [[1, 2, 0], 3],
        [[3, 4, -1, 1], 2],
        [[7, 8, 9, 11, 12], 1],
    ]
    for c in cases:
        print(c)
        res = s.firstMissingPositive(c[0])
        assert res == c[1], "expected: {}, got: {}".format(c[1], res)
