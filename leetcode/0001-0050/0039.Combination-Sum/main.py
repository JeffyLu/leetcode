class Solution:

    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        stack = [(0, [], target)]
        while stack:
            i, r, t = stack.pop()
            while i < len(candidates) and candidates[i] <= t:
                if candidates[i] == t:
                    r.append(candidates[i])
                    res.append(r)
                    break
                stack.append((i, r+[candidates[i]], t-candidates[i]))
                i += 1
        return res


if __name__ == '__main__':

    s = Solution()
    cases = [
        {
            "candidates": [2],
            "target": 1,
            "res": [
            ]
        },
        {
            "candidates": [7, 3],
            "target": 17,
            "res": [
                [3, 7, 7]
            ]
        },
        {
            "candidates": [2, 3, 6, 7],
            "target": 7,
            "res": [
                [7],
                [2, 2, 3],
            ]
        },
        {
            "candidates": [2, 3, 5],
            "target": 8,
            "res": [
                [2, 2, 2, 2],
                [2, 3, 3],
                [3, 5],
            ]
        },
    ]
    for c in cases:
        print(c)
        res = s.combinationSum(c["candidates"], c["target"])
        res.sort()
        c["res"].sort()
        assert res == c["res"], "expected: {}, got: {}".format(c["res"], res)
