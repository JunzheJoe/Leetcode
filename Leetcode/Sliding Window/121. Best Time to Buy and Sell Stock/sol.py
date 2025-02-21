from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1  # Left = buy day, Right = sell day
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r  # Move left pointer to the new minimum price
            
            r += 1  # Move right pointer

        return maxP

