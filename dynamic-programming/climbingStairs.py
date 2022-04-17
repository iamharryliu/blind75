class Solution:
    @classmethod
    def climbStairs(self, n):
        if n < 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        two_steps_before = 1
        one_step_before = 2
        all_ways = 0
        for _ in range(2, n):
            all_ways = one_step_before + two_steps_before
            two_steps_before = one_step_before
            one_step_before = all_ways

        return all_ways


result = Solution.climbStairs(4)
print(result)
