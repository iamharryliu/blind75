class Solution:
    @classmethod
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for _ in range(m - 1):
            new_dp = [1] * n
            for x in range(n - 2, -1, -1):
                new_dp[x] = new_dp[x + 1] + dp[x]
            dp = new_dp
        return dp[0]


m = 3
n = 7
output = 28
res = Solution.uniquePaths(m, n)
print(res == output)

m = 3
n = 2
output = 3
res = Solution.uniquePaths(m, n)
print(res == output)
