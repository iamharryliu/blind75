import math


class Solution:
    @classmethod
    def minWindow(self, s, t):
        if not t:
            return ""

        count_t = {}
        count_s = {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)
        have, need = 0, len(count_t)
        res = [0, math.inf]

        l = 0
        for r, c in enumerate(s):
            count_s[c] = 1 + count_s.get(c, 0)

            # increment have?
            if c in count_t and count_s[c] == count_t[c]:
                have += 1

            while have == need:

                # compare curr_len and prev_len
                curr_len = r - l + 1
                pl, pr = res
                prev_len = pr - pl + 1
                if curr_len < prev_len:
                    res = [l, r]

                # update l index and
                count_s[s[l]] -= 1
                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        # return res string if res_len is not infinity
        l, r = res
        return s[l : r + 1] if res != [0, math.inf] else ""


res = Solution.minWindow("ADOBECODEBANC", "ABC") == "BANC"
print(res)
