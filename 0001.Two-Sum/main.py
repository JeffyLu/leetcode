class Solution:

    def twoSum(self, nums, target):
        num_dict = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in num_dict:
                return [num_dict[res], i]
            num_dict[nums[i]] = i
