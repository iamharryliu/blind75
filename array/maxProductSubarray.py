class Solution:
    @classmethod
    def maxProduct(self, nums):
        res = max(nums)
        cmin, cmax = 1, 1

        for num in nums:
            if num == 0:
                cmin, cmax = 1, 1
                continue
            temp = cmax * num
            cmax = max(temp, num * cmin, num)
            cmin = min(temp, num * cmin, num)
            res = max(res, cmax)
        return res


result = Solution.maxProduct([2, 3, -2, 4])
print(result)
