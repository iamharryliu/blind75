class Solution:
    @classmethod
    def longestPalindrome(self, s: str) -> int:
        hmap = {}

        for c in s:
            hmap[c] = hmap.get(c, 0) + 1

        res = 0
        foundOdd = False
        for _, v in hmap.items():
            if v % 2 == 0:
                res += v
            if v % 2 == 1 and foundOdd:
                res += v - 1
            if v % 2 == 1 and not foundOdd:
                res += v
                foundOdd = True
        return res


print(Solution.longestPalindrome(s="abccccdd") == 7)
