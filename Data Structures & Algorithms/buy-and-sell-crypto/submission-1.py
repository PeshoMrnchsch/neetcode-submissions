class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # [10,1,5,6,7,1]
        # profit = right - left
        cheapest_seen = prices[0]
        profit = 0
        # Consider only cur day and the min price selling

        for price in prices:
            if price < cheapest_seen:
                cheapest_seen = price

            calc = price - cheapest_seen
            if calc > profit:
                profit  = calc

        return profit
