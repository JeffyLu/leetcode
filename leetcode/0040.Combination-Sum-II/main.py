class Solution:

    def combinationSum2(self, candidates, target):
        candidates.sort()
        length = len(candidates)
        res = []
        stack = [(0, [], target)]
        while stack:
            i, r, t = stack.pop()
            while i < length and candidates[i] <= t:
                if candidates[i] == t:
                    r.append(candidates[i])
                    res.append(r)
                    break
                stack.append((i+1, r+[candidates[i]], t-candidates[i]))
                while i+1 < length and candidates[i+1] == candidates[i]:
                    i += 1
                i += 1
        return res


if __name__ == "__main__":

    s = Solution()
    cases = [
        {
            "candidates": [1],
            "target": 2,
            "res": [
            ],
        },
        {
            "candidates": [10, 1, 2, 7, 6, 1, 5],
            "target": 8,
            "res": [
                [1, 7],
                [1, 2, 5],
                [2, 6],
                [1, 1, 6],
            ],
        },
        {
            "candidates": [2, 5, 2, 1, 2],
            "target": 5,
            "res": [
                [1, 2, 2],
                [5],
            ],
        },
        {
            "candidates": [1, 1, 1, 1, 1, 2, 3, 4],
            "target": 4,
            "res": [
                [1, 1, 1, 1],
                [1, 1, 2],
                [1, 3],
                [4],
            ],
        },
    ]
    for c in cases:
        print(c)
        res = s.combinationSum2(c["candidates"], c["target"])
        res.sort()
        c["res"].sort()
        assert res == c["res"], "expected: {}, got: {}".format(c["res"], res)
