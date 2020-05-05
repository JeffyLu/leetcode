class Solution:

    def permute(self, nums):
        return self._solution([], nums)

    def _solution(self, selected, candidates):
        if len(selected) == len(candidates):
            return [selected[:]]

        res = []
        for n in candidates:
            if n in selected:
                continue
            selected.append(n)
            res.extend(self._solution(selected, candidates))
            selected.pop(-1)
        return res


if __name__ == '__main__':

    cases = [
        {
            "nums": [1],
            "res": [[1]],
        },
        {
            "nums": [1, 2],
            "res": [[1, 2], [2, 1]],
        },
        {
            "nums": [1, 2, 3],
            "res": [
                [1, 2, 3], [1, 3, 2],
                [2, 1, 3], [2, 3, 1],
                [3, 1, 2], [3, 2, 1],
            ],
        },
    ]

    s = Solution()
    for c in cases:
        print(c)
        res = s.permute(c["nums"])
        res.sort()
        expected = list(sorted(c["res"]))
        assert res == expected, "expected: {}, got: {}".format(expected, res)
