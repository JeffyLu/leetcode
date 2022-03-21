class Solution:

    def firstMissingPositive(self, nums):
        length = len(nums)
        for i in range(length):
            j = nums[i] - 1
            while nums[i] > 0 and j < length and nums[j] != nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
                j = nums[i] - 1
        i = 0
        while i < length:
            if nums[i] != i+1:
                break
            i += 1
        return i + 1


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
