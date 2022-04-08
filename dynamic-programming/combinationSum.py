class Solution:
    @classmethod
    def combinationSum4(self, nums, target):
        result = []

        def dfs(i, current, total):
            print(i, current, total)
            if total == target:
                result.append(current.copy())
                return
            if i >= len(nums) or total > target:
                return
            current.append(nums)
            dfs(i, current, total + nums[i])
            current.pop()
            dfs(i + 1, current, total)

        dfs(0, [], 0)
        return result


res = len(Solution.combinationSum4([1, 2, 3], 4))
print(res)

