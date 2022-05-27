class Solution:
    @classmethod
    def jobScheduling(self, startTime, endTime, profit):
        lst = sorted(zip(startTime, endTime, profit), key=lambda x: x[1])
        dp = [[0, 0]]

        def b_search(c_start):
            l, r = 0, len(dp) - 1

            while l <= r:
                m = (l + r) // 2
                p_end_time = dp[m][0]
                if p_end_time <= c_start:
                    l = m + 1
                else:
                    r = m - 1
            return l - 1

        for start, end, profit in lst:
            i = b_search(start)
            p_profit = dp[-1][1]
            c_profit = dp[i][1] + profit
            if c_profit > p_profit:
                dp.append([end, c_profit])
        max_profit = dp[-1][1]
        return max_profit


print(
    Solution.jobScheduling(
        startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70]
    )
    == 120
)


print(
    Solution.jobScheduling(
        startTime=[1, 2, 3, 4, 6],
        endTime=[3, 5, 10, 6, 9],
        profit=[20, 20, 100, 70, 60],
    )
    == 150
)


print(
    Solution.jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4])
    == 6
)
