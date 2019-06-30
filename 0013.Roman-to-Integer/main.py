class Solution:
    def romanToInt(self, s):
        roman_to_num = {
            'M': 1000, 'CM': 900,
            'D': 500, 'CD': 400,
            'C': 100, 'XC': 90,
            'L': 50, 'XL': 40,
            'X': 10, 'IX': 9,
            'V': 5, 'IV': 4,
            'I': 1,
        }
        res = 0
        idx = 0
        while idx < len(s):
            roman = s[idx: idx+2]
            if roman_to_num.get(roman, None) is not None:
                res += roman_to_num[roman]
                idx += 2
                continue
            roman = s[idx]
            res += roman_to_num[roman]
            idx += 1
        return res


if __name__ == '__main__':

    cases = [
        [3, 'III'],
        [4, 'IV'],
        [9, 'IX'],
        [58, 'LVIII'],
        [1994, 'MCMXCIV'],
    ]
    s = Solution()
    for case in cases:
        res = s.romanToInt(case[1])
        assert res == case[0], 'expected: {}, got: {}'.format(case[0], res)
