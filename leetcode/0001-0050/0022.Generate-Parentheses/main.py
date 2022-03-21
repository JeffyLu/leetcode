class Solution:

    def generateParenthesis(self, n):
        if n <= 0:
            return []
        if n == 1:
            return ['()']
        tmp = self.generateParenthesis(n-1)
        res = set()
        for r in tmp:
            for i in range((n-1)*2+1):
                res.add('{}(){}'.format(r[:i], r[i:]))
        return list(res)


if __name__ == '__main__':

    s = Solution()
    cases = [
        [0, []],
        [1, [
            "()",
        ]],
        [2, [
            "()()",
            "(())",
        ]],
        [3, [
            "((()))",
            "(()())",
            "(())()",
            "()(())",
            "()()()",
        ]],
    ]
    for c in cases:
        res = s.generateParenthesis(c[0])
        res.sort()
        c[1].sort()
        assert res == c[1], 'expected: {}, got: {}'.format(c[1], res)
