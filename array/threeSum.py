class Solution:
    @classmethod
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i, num in enumerate(nums):

            if i > 0 and num == nums[i - 1]:  # skip index if same as previous number
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = num + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                if three_sum > 0:
                    r -= 1
                if three_sum == 0:
                    res.append((num, nums[l], nums[r]))
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:  # skip similar l values
                        l += 1

        return res


test_value = [-1, -1, 0, 1, 2, -1, -4]
result = Solution.threeSum(test_value) == [(-1, -1, 2), (-1, 0, 1)]
print(result)
