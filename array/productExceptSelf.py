class Solution:
    @classmethod
    def productExceptSelf(self, nums):

        # Product numbers before element
        p = 1
        output = []
        for num in nums:
            output.append(p)
            p = p * num

        # Product of numbers after element
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * p
            p *= nums[i]
        return output


nums = [1, 2, 3, 4, 5]
result = Solution.productExceptSelf(nums)
print(result)
