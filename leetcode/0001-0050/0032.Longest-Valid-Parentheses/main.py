class Solution:

    def longestValidParentheses(self, s):
        buf = []
        stack = []
        for i in range(len(s)):
            if s[i] == '(' or not stack or s[stack[-1]] == ')':
                stack.append(i)
                continue
            stack.pop()
            buf.append(i)

        i = 0
        j = 0
        res = 0
        while i < len(stack):
            tmp = 0
            while j < len(buf):
                if buf[j] < stack[i]:
                    tmp += 2
                    j += 1
                    continue
                break
            if tmp > res:
                res = tmp
            i += 1
        if j <= len(buf) - 1:
            tmp = 2 * (len(buf) - j)
            if tmp > res:
                res = tmp
        return res


if __name__ == '__main__':

    from test import case1, answer1
    s = Solution()
    cases = [
        ['(()', 2],
        [')()())', 4],
        ['()())()', 4],
        [')()())()()()', 6],
        [')()()(((()))', 6],
        [')()())()()(', 4],
        [case1, answer1],
    ]
    for c in cases:
        res = s.longestValidParentheses(c[0])
        assert res == c[1], 'expected: {}, got: {}'.format(c[1], res)
