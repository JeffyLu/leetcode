class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        length = len(nums)
        closest = None
        res = None
        for i in range(length-2):
            for j in range(i+1, length-1):
                closest_target = target - nums[i] - nums[j]
                if closest_target > 0:
                    for x in range(length-1, j, -1):
                        distance = closest_target - nums[x]
                        if closest is None or abs(distance) < closest:
                            res = nums[i] + nums[j] + nums[x]
                            closest = abs(distance)
                        if distance > 0:
                            break
                        elif distance == 0:
                            return target
                else:
                    for x in range(j+1, length):
                        distance = closest_target - nums[x]
                        if closest is None or abs(distance) < closest:
                            res = nums[i] + nums[j] + nums[x]
                            closest = abs(distance)
                        if distance < 0:
                            break
                        elif distance == 0:
                            return target
        return res


if __name__ == '__main__':

    cases = [
        [[-1, 2, 1, -4], 1, 2],
        [[0, 5, -1, -2, 4, -1, 0, -3, 4, -5], 1, 1],
        [[1, 1, -1, -1, 3], -1, -1],
        [[-55, -24, -18, -11, -7, -3, 4, 5, 6, 9, 11, 23, 33], 0, 0],
        [[4, 5, 6, 9, 11, 23, 33], 0, 15],
    ]
    s = Solution()
    for case in cases:
        res = s.threeSumClosest(case[0], case[1])
        assert res == case[2], 'expected: {}, got: {}'.format(case[2], res)
