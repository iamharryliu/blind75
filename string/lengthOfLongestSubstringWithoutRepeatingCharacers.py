class Solution:
    @classmethod
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        maxLength = 0
        for c in s:
            if c in substring:
                substring = substring[substring.index(c) + 1 :]
            substring += c
            maxLength = max(maxLength, len(substring))
        return maxLength


test = "abcabcbb"
expected_res = 3
print(Solution.lengthOfLongestSubstring(test) == expected_res)
