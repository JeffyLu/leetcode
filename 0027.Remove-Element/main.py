class Solution:

    def removeElement(self, nums, val):
        length = len(nums)
        if length == 0:
            return 0
        i = 0
        j = 0
        while j < length:
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
            j += 1
        return i


if __name__ == '__main__':

    s = Solution()
    cases = [
        [[], 3, 0, []],
        [[1], 1, 0, []],
        [[1], 2, 1, [1]],
        [[3, 2, 2, 3], 3, 2, [2, 2]],
        [[0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 1, 3, 0, 4]],
    ]
    for c in cases:
        res = s.removeElement(c[0], c[1])
        assert res == c[2], 'expect length: {}, got: {}'.format(c[2], res)
        assert c[0][:res] == c[3], 'expect arr: {}, got: {}'.format(c[0], c[3])
