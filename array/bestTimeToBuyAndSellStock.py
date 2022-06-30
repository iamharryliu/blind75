from typing import List


class Solution:
    @classmethod
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for price in prices[1:]:
            maxProfit = max(maxProfit, price - minPrice)
            minPrice = min(price, minPrice)
        return maxProfit


print(Solution.maxProfit(prices=[7, 1, 5, 3, 6, 4]) == 5)
print(Solution.maxProfit(prices=[7, 6, 4, 3, 1]) == 0)
