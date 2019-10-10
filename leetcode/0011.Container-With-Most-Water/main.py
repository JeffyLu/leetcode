class Solution:

    def maxArea(self, height):
        res = 0
        left, right = 0, len(height) - 1
        while left < right:
            min_height = min(height[left], height[right])
            area = min_height * (right-left)
            if area > res:
                res = area

            got_next = False
            if height[left] == min_height:
                for i in range(left+1, right):
                    if height[i] > min_height:
                        left = i
                        got_next = True
                        break
            else:
                for i in range(right-1, left, -1):
                    if height[i] > min_height:
                        right = i
                        got_next = True
                        break
            if not got_next:
                break
        return res


if __name__ == '__main__':

    s = Solution()
    cases = [
        [[1, 8, 6, 2, 5, 4, 8, 3, 7], 49],
    ]
    for case in cases:
        res = s.maxArea(case[0])
        assert res == case[1], 'expected: {}, got: {}'.format(case[1], res)
