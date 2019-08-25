class Solution:

    def searchRange(self, nums, target):
        left = 0
        right = len(nums) - 1
        res = [-1, -1]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                for i in range(mid, right+1):
                    if nums[i] != target:
                        res[1] = i - 1
                        break
                    elif i == right:
                        res[1] = i
                        break
                for i in range(mid, left-1, -1):
                    if nums[i] != target:
                        res[0] = i + 1
                        break
                    elif i == left:
                        res[0] = i
                        break
                return res
            elif nums[mid] > target:
                for i in range(mid-1, left-2, -1):
                    right = i
                    if i < 0 or nums[i] != nums[mid]:
                        break
            else:
                for i in range(mid+1, right+2):
                    left = i
                    if i > right or nums[i] != nums[mid]:
                        break
        return res


if __name__ == '__main__':

    s = Solution()
    cases = [
        [[], 1, [-1, -1]],
        [[1], 1, [0, 0]],
        [[1], 2, [-1, -1]],
        [[1], 0, [-1, -1]],
        [[1, 1, 1], 0, [-1, -1]],
        [[5, 7, 7, 8, 8, 10], 8, [3, 4]],
        [[5, 7, 7, 8, 8, 10], 6, [-1, -1]],
    ]
    for c in cases:
        print(c)
        res = s.searchRange(c[0], c[1])
        assert res == c[2], 'expected: {}, got: {}'.format(c[2], res)
