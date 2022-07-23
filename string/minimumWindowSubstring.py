import math


class Solution:
    @classmethod
    def minWindow(self, s, t):
        smap = {}
        tmap = {}
        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)
        have = 0
        need = len(tmap)
        res = [0, math.inf]

        l = 0
        for r, c in enumerate(s):
            smap[c] = smap.get(c, 0) + 1
            if c in tmap and smap[c] == tmap[c]:
                have += 1
            while have == need:
                pl, pr = res
                if r - l < pr - pl:
                    res = [l, r + 1]
                smap[s[l]] -= 1
                if s[l] in t and smap[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r] if r != math.inf else ""


s = "ADOBECODEBANC"
t = "ABC"
output = "BANC"
res = Solution.minWindow(s, t)
print(res == output)

s = "a"
t = "a"
output = "a"
res = Solution.minWindow(s, t)
print(res == output)


s = "a"
t = "aa"
output = ""
res = Solution.minWindow(s, t)
print(res == output)
