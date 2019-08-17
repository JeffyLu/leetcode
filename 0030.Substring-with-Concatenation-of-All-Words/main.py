class Solution:

    def findSubstring(self, s, words):
        if not s or not words:
            return []

        len_s = len(s)
        len_w = len(words[0])
        cnt_w = len(words)
        word_stat = dict()
        for w in words:
            if w in word_stat:
                word_stat[w] += 1
            else:
                word_stat[w] = 1
        res = []
        i = 0
        while i <= len_s - len_w * cnt_w:
            matched = dict()
            flag = True
            for j in range(cnt_w):
                w = s[i+j*len_w:i+(j+1)*len_w]
                if w not in word_stat:
                    flag = False
                    break
                if w in matched:
                    matched[w] += 1
                    if matched[w] > word_stat[w]:
                        flag = False
                        break
                else:
                    matched[w] = 1
            if flag:
                res.append(i)
            i += 1

        return res


if __name__ == '__main__':

    s = Solution()
    cases = [
        ["foobar", ["foo", "bar"], [0]],
        ["barfoothefoobarman", ["foo", "bar"], [0, 9]],
        ["wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []],
        ["barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]],
        ["wordgoodgoodgoodbestword", ["word", "good", "best", "good"], [8]],
    ]
    for c in cases:
        print(c)
        res = s.findSubstring(c[0], c[1])
        res.sort()
        assert res == c[2], 'expected: {}, got: {}'.format(c[2], res)
