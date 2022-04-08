class Solution:
    @classmethod
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                wordFitsInString = (i + len(word)) <= len(s)
                if wordFitsInString and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]  # set dp to previous dp if word fits
                if dp[i]:
                    break  # break out of loop if there is a passage to end
        return dp[0]


print(Solution.wordBreak("leetcode", ["leet", "code"]))

