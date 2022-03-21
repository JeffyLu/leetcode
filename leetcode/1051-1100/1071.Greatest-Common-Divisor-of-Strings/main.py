class Solution:

    def gcdOfStrings(self, str1, str2):
        len1, len2 = len(str1), len(str2)
        if len1 > len2:
            str1, str2 = str2, str1
            len1, len2 = len2, len1
        res = -1
        for i in range(len1):
            if len1 % (i+1) != 0 or len2 % (i+1) != 0:
                continue
            flag = True
            for x in range(i+1, len1):
                if str1[x] != str1[x % (i+1)]:
                    flag = False
                    break
            if not flag:
                continue
            for y in range(len2):
                if str2[y] != str1[y % (i+1)]:
                    flag = False
                    break
            if flag:
                res = i
        return str1[:res+1]


if __name__ == '__main__':

    cases = [
        ['abcabc', 'abc', 'abc'],
        ['ababab', 'abab', 'ab'],
        ['life', 'code', ''],
    ]
    s = Solution()
    for c in cases:
        res = s.gcdOfStrings(c[0], c[1])
        assert res == c[2], 'expected: {}, got: {}'.format(c[2], res)
