class Solution:
    @classmethod
    def longestPalindrome(self, s):
        res = ""

        for i in range(len(s)):
            # odd case, like "aba"
            tmp = Solution.helper(s, i, i)
            if len(tmp) > len(res):
                res = tmp

            # even case, like "abba"
            tmp = Solution.helper(s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp

        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    @classmethod
    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1 : right]


result = Solution.longestPalindrome("babad")
print(result)
