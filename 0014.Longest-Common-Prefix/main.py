class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ''
        elif len(strs) == 1:
            return strs[0]

        min_len = len(strs[0])
        for s in strs[1:]:
            length = len(s)
            if length < min_len:
                min_len = length

        res = ''
        for i in range(min_len):
            prefix = strs[0][i]
            for s in strs[1:]:
                if s[i] != prefix:
                    return res
            res += prefix
        return res


if __name__ == '__main__':

    cases = [
        [['flower', 'flow', 'flight'], 'fl'],
        [['dog', 'racecar', 'car'], ''],
    ]
    s = Solution()
    for case in cases:
        res = s.longestCommonPrefix(case[0])
        assert res == case[1], 'expected: {}, got: {}'.format(case[1], res)
