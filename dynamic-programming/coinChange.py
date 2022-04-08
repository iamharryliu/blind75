class Solution:
    @classmethod
    def coinChange(self, coins, amount):
        # set array with initial value (amount + 1) which will be used to verify that change can be made from the amount
        dp = [amount + 1]
        dp[0] = 0

        # Loop thought amounts and change
        for a in range(1, amount + 1):
            for coin in coins:
                # If difference is greater than 0 dp smaller value
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])

        # return dp[amount] but if it's equal to initial value that means that change could not be created from the given coins
        return dp[amount] if dp[amount] != amount + 1 else -1


result = Solution.coinChange([1, 2, 5], 11)
print(result)
