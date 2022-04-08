class Solution:
    @classmethod
    def minWindow(self, s, t):

        # return empty string if t is empty
        if t == "":
            return ""

        # count the characters in string t
        window, count_t = {}, {}
        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        # track have, need, res, resLen
        have, need = 0, len(count_t)
        res = [-1, -1]
        res_len = float("infinity")

        l = 0
        for r in range(len(s)):

            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                if r - l + 1 < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # remove left index character from window
                # check if condition is still satisfied, if not decrement have
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        # return res string if res_len is not infinity
        l, r = res
        return s[l : r + 1] if res_len != float("infinity") else ""


res = Solution.minWindow("ADOBECODEBANC", "ABC")
print(res)
