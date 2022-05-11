class Solution:
    @classmethod
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = ""
        l = 0
        maxLength = 0
        for c in s:
            while c in substring:
                substring = substring[1:]
                l += 1
            substring += c
            maxLength = max(maxLength, len(substring))
        return maxLength


test = "abcabcbb"
expected_res = 3
print(Solution.lengthOfLongestSubstring(test))
