from typing import List


class Solution:
    @classmethod
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or total > target:
                return

            cur.append(candidates[i])
            dfs(i, cur, sum(cur))
            cur.remove(candidates[i])
            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return res


print(Solution.combinationSum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]])
