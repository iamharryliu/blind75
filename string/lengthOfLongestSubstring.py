class Solution(object):
    @classmethod
    def lengthOfLongestSubstring(self, s):
        start = maxLength = 0
        store = {}
        for i, char in enumerate(s):
            # change start only if value in store and store value is greater than start
            if char in store and store[char] >= start:
                start = store[char] + 1
            # change max
            maxLength = max(maxLength, i - start + 1)
            # update store
            store[char] = i
        return maxLength


test = "abcabcbb"
print(Solution.lengthOfLongestSubstring(test))
