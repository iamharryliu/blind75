class Solution:
    @classmethod
    def twoSum(self, nums, target):
        store = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in store:
                return [i, store[diff]]
            else:
                store[num] = i


result = Solution.twoSum([2, 7, 11, 15], 9)
print(result)
