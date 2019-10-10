class Solution:

    def threeSum(self, nums):
        res = []
        nums.sort()
        length = len(nums)
        nums_idx = {val: i for i, val in enumerate(nums)}
        last1 = None
        for i in range(length-2):
            if nums[i] > 0:
                break
            if last1 == nums[i]:
                continue
            last1 = nums[i]
            last2 = None
            for j in range(i+1, length-1):
                if last2 == nums[j]:
                    continue
                last2 = nums[j]
                target = 0 - nums[i] - nums[j]
                if target < 0:
                    break
                target_idx = nums_idx.get(target, -1)
                if target_idx > j:
                    res.append([nums[i], nums[j], target])
        return res


if __name__ == '__main__':

    cases = [
        {
            'nums': [-1, 0, 1, 2, -1, -4],
            'ans': [
                [-1, -1, 2],
                [-1, 0, 1],
            ],
        },
        {
            'nums': [1, 1, -2],
            'ans': [
                [-2, 1, 1],
            ],
        },
        {
            'nums': [0, 0, 0, 0],
            'ans': [
                [0, 0, 0],
            ],
        },
        {
            'nums': [-2, 0, 1, 1, 2],
            'ans': [
                [-2, 0, 2],
                [-2, 1, 1],
            ],
        },
        {
            'nums': [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
            'ans': [
                [-4, -2, 6],
                [-4, 0, 4],
                [-4, 1, 3],
                [-4, 2, 2],
                [-2, -2, 4],
                [-2, 0, 2],
            ],
        },
    ]
    s = Solution()
    for case in cases:
        res = s.threeSum(case['nums'])
        assert res == case['ans'], 'expected: {}, got: {}'.format(
            case['ans'], res)
