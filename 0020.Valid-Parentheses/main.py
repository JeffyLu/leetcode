class Solution:

    def isValid(self, brackets):
        if not brackets:
            return True

        stack = []
        for s in brackets:
            if s in ('(', '[', '{'):
                stack.append(s)
                continue

            if len(stack) == 0:
                return False
            left = stack.pop()
            if s == ']' and left == '[':
                continue
            elif s == ')' and left == '(':
                continue
            elif s == '}' and left == '{':
                continue
            else:
                return False
        return len(stack) == 0


if __name__ == '__main__':

    s = Solution()
    cases = [
        ["()", True],
        ["()[]{}", True],
        ["(]", False],
        ["([)]", False],
        ["{[]}", True],
    ]
    for c in cases:
        res = s.isValid(c[0])
        assert res == c[1], 'expected: {}, got: {}'.format(c[1], res)
