class Solution:

    def permuteUnique(self, nums):
        return self._solution([], set(), list(sorted(nums)))

    def _solution(self, selected, selectedIdx, candidates):
        if len(selected) == len(candidates):
            return [selected[:]]

        res = []
        poped = None
        for i in range(len(candidates)):
            if i in selectedIdx or candidates[i] == poped:
                continue
            selected.append(candidates[i])
            selectedIdx.add(i)
            res.extend(self._solution(selected, selectedIdx, candidates))
            poped = selected.pop(-1)
            selectedIdx.remove(i)
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
            "nums": [1, 1, 2],
            "res": [
                [1, 1, 2], [1, 2, 1], [2, 1, 1],
            ],
        },
    ]

    s = Solution()
    for c in cases:
        print(c)
        res = s.permuteUnique(c["nums"])
        res.sort()
        expected = list(sorted(c["res"]))
        assert res == expected, "expected: {}, got: {}".format(expected, res)
