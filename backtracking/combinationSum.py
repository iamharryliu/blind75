from typing import List


class Solution:
    @classmethod
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur):
            if sum(cur) == target:
                res.append(cur.copy())
                return
            if i >= len(candidates) or sum(cur) > target:
                return

            cur.append(candidates[i])
            dfs(i, cur)
            cur.remove(candidates[i])
            dfs(i + 1, cur)

        dfs(0, [])
        return res


print(Solution.combinationSum(candidates=[2, 3, 6, 7], target=7) == [[2, 2, 3], [7]])
