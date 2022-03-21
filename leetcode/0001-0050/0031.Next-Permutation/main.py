class Solution:

    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        reverse = True
        for i in range(len(nums)-1, 0, -1):
            if nums[i] <= nums[i-1]:
                continue
            min_idx = i
            for m in range(len(nums)-1, i, -1):
                if nums[m] > nums[i-1]:
                    min_idx = m
                    break
            nums[i-1], nums[min_idx] = nums[min_idx], nums[i-1]
            for x in range(i, len(nums)-1):
                tmp = x + 1
                for y in range(tmp, len(nums)):
                    if nums[y] < nums[tmp]:
                        tmp = y
                if nums[x] > nums[tmp]:
                    nums[tmp], nums[x] = nums[x], nums[tmp]
            reverse = False
            break

        if reverse:
            nums.sort()


if __name__ == '__main__':

    s = Solution()
    cases = [
        [[1, 2, 3], [1, 3, 2]],
        [[3, 2, 1], [1, 2, 3]],
        [[1, 1, 5], [1, 5, 1]],
        [[1, 3, 0], [3, 0, 1]],
        [[1, 3, 2], [2, 1, 3]],
        [[1, 3, 2, 2], [2, 1, 2, 3]],
    ]
    for c in cases:
        print(c)
        s.nextPermutation(c[0])
        assert c[0] == c[1], 'expected: {}, got: {}'.format(c[1], c[0])
