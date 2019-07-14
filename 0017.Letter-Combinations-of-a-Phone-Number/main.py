class Solution:
    def letterCombinations(self, digits):
        if len(digits) == 0:
            return []

        digit_to_chars = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = ['']
        for d in digits:
            chars = digit_to_chars[d]
            temp = []
            for c in chars:
                for r in res:
                    temp.append(r+c)
            res = temp

        return res


if __name__ == '__main__':

    cases = [
        ['23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'].sort()],
    ]
    s = Solution()
    for case in cases:
        res = s.letterCombinations(case[0]).sort()
        assert res == case[1], 'expected: {}, got: {}'.format(case[1], res)
