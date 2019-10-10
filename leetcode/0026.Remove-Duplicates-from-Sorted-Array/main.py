class Solution:

    def removeDuplicates(self, nums):
        length = len(nums)
        if length == 0:
            return length
        i = 0
        j = i+1
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i+1


if __name__ == '__main__':

    s = Solution()
    cases = [
        [[], 0, []],
        [[1], 1, [1]],
        [[1, 1, 2], 2, [1, 2]],
        [[0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]],
    ]
    for c in cases:
        length = s.removeDuplicates(c[0])
        assert length == c[1], 'expect length: {}, got length: {}'.format(
            c[1], length)
        assert c[0][:length] == c[2], 'except arr: {}, got arr: {}'.format(
            c[2], c[0])
