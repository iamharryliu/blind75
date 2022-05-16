from typing import List


class Solution:
    @classmethod
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        hmap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def dfs(i, word):
            if len(word) == len(digits):
                res.append(word)
            else:
                for c in hmap[digits[i]]:
                    dfs(i + 1, word + c)

        if digits:
            dfs(0, "")
        return res


print(
    Solution.letterCombinations("23")
    == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
)
