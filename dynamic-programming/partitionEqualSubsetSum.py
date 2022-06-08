from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        dp = set([0])
        target = sum(nums) // 2

        for num in nums:
            new_dp = set()
            for p_sum in dp:
                new_dp.add(p_sum + num)
                new_dp.add(p_sum)
            dp = new_dp

        return target in dp
