class Solution:
    @classmethod
    def threeSum(self, nums):
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            # skip index if same as previous number
            if i > 0 and num == nums[i - 1]:
                continue

            # set left and right indices
            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = num + nums[left] + nums[right]

                # advance left and right indice depending on three sum value
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1

                else:
                    # if three_sum equals 0 add to result
                    res.append((num, nums[left], nums[right]))

                    # advance left until it is not same as previous value
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return res


test_value = [-1, -1, 0, 1, 2, -1, -4]
result = Solution.threeSum(test_value)
print(result)
