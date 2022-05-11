class Solution:
    @classmethod
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            num = nums[mid]
            if target == num:
                return mid

            if nums[l] <= num:
                if num < target or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1

            else:
                if target < num or nums[r] < target:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


res = Solution.search([4, 5, 6, 7, 0, 1, 2], 0)
expected_res = 4
print(res == expected_res)
