class Solution:

    def searchInsert(self, nums, target):
        if not nums:
            return 0

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left if nums[left] >= target else left + 1


if __name__ == '__main__':

    s = Solution()
    cases = [
        [[], 1, 0],
        [[1], 0, 0],
        [[1], 1, 0],
        [[1], 2, 1],
        [[1, 3, 5, 6], 5, 2],
        [[1, 3, 5, 6], 2, 1],
        [[1, 3, 5, 6], 7, 4],
        [[1, 3, 5, 6], 0, 0],
    ]
    for c in cases:
        print(c)
        res = s.searchInsert(c[0], c[1])
        assert res == c[2], 'expected: {}, got: {}'.format(c[2], res)
