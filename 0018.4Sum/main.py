class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        num_idx = {val: i for i, val in enumerate(nums)}
        res = []
        last_x = None
        for x in range(len(nums)-3):
            if last_x is not None and nums[x] == last_x:
                continue
            last_x = nums[x]
            last_y = None
            for y in range(x+1, len(nums)-2):
                if last_y is not None and nums[y] == last_y:
                    continue
                last_y = nums[y]
                last_z = None
                for z in range(y+1, len(nums)-1):
                    if last_z is not None and nums[z] == last_z:
                        continue
                    last_z = nums[z]
                    last_num_idx = num_idx.get(
                        target-nums[x]-nums[y]-nums[z], None)
                    if last_num_idx is not None and last_num_idx > z:
                        res.append(
                            [nums[x], nums[y], nums[z], nums[last_num_idx]])
        return res


if __name__ == '__main__':

    s = Solution()
    cases = [
        {
            'nums': [5, 5, 3, 5, 1, -5, 1, -2],
            'target': 4,
            'res': [
                [-5, 1, 3, 5],
            ],
        },
        {
            'nums': [1, 0, -1, 0, -2, 2],
            'target': 0,
            'res': [
                [-1,  0, 0, 1],
                [-2, -1, 1, 2],
                [-2,  0, 0, 2],
            ],
        },
        {
            'nums': [0, 0, 0, 0, 0, 0],
            'target': 0,
            'res': [
                [0, 0, 0, 0],
            ],
        },
        {
            'nums': [-3, -2, -1, 0, 0, 1, 2, 3],
            'target': 0,
            'res': [
                [-3, -2, 2, 3],
                [-3, -1, 1, 3],
                [-3, 0, 0, 3],
                [-3, 0, 1, 2],
                [-2, -1, 0, 3],
                [-2, -1, 1, 2],
                [-2, 0, 0, 2],
                [-1, 0, 0, 1],
            ],
        },
    ]
    for case in cases:
        res = s.fourSum(case['nums'], case['target'])
        res.sort()
        case['res'].sort()
        assert res == case['res'], 'expected: {}, got: {}'.format(
            case['res'], res)
