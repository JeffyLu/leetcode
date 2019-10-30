class Solution:

    def countAndSay(self, n):
        if n <= 1:
            return "1"
        last = self.countAndSay(n-1)
        cnt = 1
        res = ""
        for i in range(1, len(last)):
            if last[i] == last[i-1]:
                cnt += 1
                continue
            res += "{}{}".format(cnt, last[i-1])
            cnt = 1
        res += "{}{}".format(cnt, last[len(last)-1])
        return res


if __name__ == '__main__':

    s = Solution()
    cases = [
        [1, "1"],
        [2, "11"],
        [3, "21"],
        [4, "1211"],
        [5, "111221"],
        [6, "312211"],
        [7, "13112221"],
        [8, "1113213211"],
        [9, "31131211131221"],
        [10, "13211311123113112211"],
    ]
    for c in cases:
        print(c)
        res = s.countAndSay(c[0])
        assert res == c[1], "expected: {}, got: {}".format(c[1], res)
