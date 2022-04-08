class Solution:
    @classmethod
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # search left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            # search right sorted portion
            else:
                # [1,2,3]
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


res = Solution.search([4, 5, 6, 7, 0, 1, 2], 0)
print(res)
