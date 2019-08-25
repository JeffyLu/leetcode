class Solution:

    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                if target > nums[right]:
                    right = mid - 1
                elif target < nums[right]:
                    if nums[mid] < nums[right]:
                        right = mid - 1
                        continue
                    i = mid - 1
                    while i >= 0 and nums[i] < nums[i+1]:
                        if nums[i] == target:
                            return i
                        i -= 1
                    left = mid + 1
                else:
                    return right
            else:
                if target < nums[left]:
                    left = mid + 1
                elif target > nums[left]:
                    if nums[mid] < nums[left]:
                        right = mid - 1
                        continue
                    i = mid + 1
                    while i < len(nums) and nums[i] > nums[i-1]:
                        if nums[i] == target:
                            return i
                        i += 1
                    left = mid + 1
                else:
                    return left
        return -1


if __name__ == '__main__':

    s = Solution()
    cases = [
        [[1, 3], 2, -1],
        [[5, 1, 3], 5, 0],
        [[3, 5, 1], 1, 2],
        [[1, 3], 0, -1],
        [[3, 1], 0, -1],
        [[1], 0, -1],
        [[1], 2, -1],
        [[4, 5, 6, 7, 0, 1, 2], 0, 4],
        [[4, 5, 6, 7, 0, 1, 2], 3, -1],

        [[4, 5, 6, 7, 0, 1, 2], 5, 1],
        [[4, 5, 6, 7, 0, 1, 2], 1, 5],
        [[5, 6, 0, 1, 2, 3, 4], 0, 2],


        [[4, 5, 6, 7, 8, 1, 2], 8, 4],
        [[4, 5, 6, 0, 1, 2, 3], 4, 0],
        [[4, 5, 6, 0, 1, 2, 3], 2, 5],
    ]
    for c in cases:
        print(c)
        res = s.search(c[0], c[1])
        assert res == c[2], 'expected: {}, got: {}'.format(c[2], res)
