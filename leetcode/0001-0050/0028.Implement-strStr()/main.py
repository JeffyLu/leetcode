class Solution:

    def strStr(self, haystack, needle):
        if needle == '':
            return 0
        i = 0
        end = len(haystack) - len(needle)
        while i <= end:
            if haystack[i] != needle[0]:
                i += 1
                continue
            flag = True
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    flag = False
                    break
            if flag:
                return i
            i += 1
        return -1


if __name__ == '__main__':

    s = Solution()
    cases = [
        ['abc', '', 0],
        ['', 'a', -1],
        ['abc', 'd', -1],
        ['abc', 'abc', 0],
        ['abcdeabcde', 'ab', 0],
        ['hello', 'll', 2],
        ['aaaaa', 'bba', -1],
        ['mississippi', 'issip', 4]
    ]
    for c in cases:
        print(c)
        res = s.strStr(c[0], c[1])
        assert res == c[2], 'expected: {}, got: {}'.format(c[2], res)
