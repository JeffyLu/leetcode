class Solution:
    def heightChecker(self, heights):
        res = 0
        for i in range(len(heights)-1):
            low = i + 1
            for j in range(low+1, len(heights)):
                if heights[j] < heights[low]:
                    low = j
            if heights[low] < heights[i]:
                heights[low], heights[i] = heights[i], heights[low]
                res += 1
        return res + 1 if res != 0 else 0


if __name__ == '__main__':

    heights = [1, 2, 1, 2, 1, 1, 1, 2, 1]
    print(Solution().heightChecker(heights))
