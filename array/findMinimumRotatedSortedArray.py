class Solution:
    @classmethod
    def findMin(self, nums):
        minimumNumber = nums[0]
        left, right = 0, len(nums) - 1
        while left <= right:

            # You know you are in the smaller array so you can compare the minimumNumber and left
            if nums[left] < nums[right]:
                return min(minimumNumber, nums[left])

            mid = (left + right) // 2
            minimumNumber = min(minimumNumber, nums[mid])
            # Search right if mid is a part of the left portion than left else search left
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        return minimumNumber


res = Solution.findMin([3, 4, 5, 1, 2])
print(res)
