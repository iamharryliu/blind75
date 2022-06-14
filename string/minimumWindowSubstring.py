import math


class Solution:
    @classmethod
    def minWindow(self, s, t):
        smap = {}
        tmap = {}
        for c in t:
            tmap[c] = 1 + tmap.get(c, 0)
        have, need = 0, len(tmap)
        res = [0, math.inf]

        l = 0
        for r, c in enumerate(s):
            smap[c] = 1 + smap.get(c, 0)
            if c in tmap and smap[c] == tmap[c]:
                have += 1
            while have == need:
                pl, pr = res
                if r - l < pr - pl:
                    res = [l, r]
                smap[s[l]] -= 1
                if s[l] in tmap and smap[s[l]] < tmap[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if res != [0, math.inf] else ""


res = Solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
print(res)
