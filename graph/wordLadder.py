from collections import defaultdict
from typing import List


class Solution:
    @classmethod
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                adj_list[word[0:i] + "*" + word[i + 1 :]].append(word)

        q = [beginWord]
        visited = set()
        res = 0

        while q:
            res += 1
            new_q = []
            for word in q:
                if word == endWord:
                    return res
                for i in range(len(word)):
                    x = word[0:i] + "*" + word[i + 1 :]
                    for newWord in adj_list[x]:
                        if newWord not in visited:
                            new_q.append(newWord)
                            visited.add(newWord)
                    visited.add(x)
            q = new_q
        return 0


print(
    Solution.ladderLength(
        beginWord="hit",
        endWord="cog",
        wordList=["hot", "dot", "dog", "lot", "log", "cog"],
    )
    == 5
)

print(
    Solution.ladderLength(
        beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log"]
    )
    == 0
)
