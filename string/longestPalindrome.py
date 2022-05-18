class Solution:
    @classmethod
    def longestPalindrome(self, s: str) -> int:
        hmap = {}

        for c in s:
            hmap[c] = hmap.get(c, 0) + 1

        res = 0
        max_odd = 0
        for k, v in hmap.items():
            if v % 2 == 0:
                res += v
            else:
                max_odd = max(max_odd, v)

        return res + max_odd


print(Solution.longestPalindrome(s="abccccdd") == 7)
