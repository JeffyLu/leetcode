class Solution:
    def smallestRepunitDivByK(self, K):
        if K & 1 == 0 or K % 5 == 0:
            return -1
        val = 0
        for i in range(1, K+1):
            val = (val * 10 + 1) % K
            if val == 0:
                return i
        return -1
