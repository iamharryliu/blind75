from typing import List


class Solution:
    @classmethod
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # less complicated answer using set
        res = set()
        nums.sort()
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l += 1
                if total < 0:
                    l += 1
                if total > 0:
                    r -= 1

        return [list(l) for l in res]

        # index skipping
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                if three_sum > 0:
                    r -= 1
                if three_sum == 0:
                    res.append((num, nums[l], nums[r]))
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res


nums = [-1, -1, 0, 1, 2, -1, -4]
output = [(-1, -1, 2), (-1, 0, 1)]
res = Solution.threeSum(nums)
print(res == output)

nums = []
output = []
res = Solution.threeSum(nums)
print(res == output)

nums = [0]
output = []
res = Solution.threeSum(nums)
print(res == output)
