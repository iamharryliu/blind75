class Solution:
    @classmethod
    def maxProduct(self, nums):
        result = max(nums)
        currentMin, currentMax = 1, 1

        for n in nums:
            if n == 0:
                currentMin, currentMax = 1, 1
                continue
            temp = currentMax * n
            currentMax = max(n * currentMax, n * currentMin, n)
            currentMin = min(temp, n * currentMin, n)
            result = max(result, currentMax)
        return result


result = Solution.maxProduct([2, 3, -2, 4])
print(result)
