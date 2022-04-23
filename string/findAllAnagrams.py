from typing import List


class Solution:
    @classmethod
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_count = {}
        s_count = {}
        res = []

        for c in p:
            p_count[c] = p_count.get(c, 0) + 1

        for i, c in enumerate(s):
            s_count[c] = s_count.get(c, 0) + 1
            if i >= len(p):
                s_count[s[i - len(p)]] -= 1
                if s_count[s[i - len(p)]] == 0:
                    s_count.pop(s[i - len(p)])
            if s_count == p_count:
                res.append(i - len(p) + 1)
        return res


res = Solution.findAnagrams(s="cbaebabacd", p="abc")
print(res == [0, 6])

