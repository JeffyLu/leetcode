class Solution:
    def intToRoman(self, num):
        nums = [
            1000, 900,
            500, 400,
            100, 90,
            50, 40,
            10, 9,
            5, 4,
            1,
        ]
        num_to_roman = {
            1000: 'M', 900: 'CM',
            500: 'D', 400: 'CD',
            100: 'C', 90: 'XC',
            50: 'L', 40: 'XL',
            10: 'X', 9: 'IX',
            5: 'V', 4: 'IV',
            1: 'I',
        }
        if num_to_roman.get(num, None) is not None:
            return num_to_roman[num]

        res = ''
        for i in nums:
            while i <= num:
                num -= i
                res += num_to_roman[i]
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
        res = s.intToRoman(case[0])
        assert res == case[1], 'expected: {}, got: {}'.format(case[1], res)
