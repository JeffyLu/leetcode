class Solution:

    def removeDuplicates(self, nums):
        length = len(nums)
        i = 0
        while i+1 < length:
            if nums[i] != nums[i+1]:
                i += 1
                continue
            nums.remove(nums[i])
            length -= 1
        return length


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
        assert c[0] == c[2], 'except arr: {}, got arr: {}'.format(
            c[2], c[0])
