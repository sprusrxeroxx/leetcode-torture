# PROBLEM STATEMENT

## 121. Best Time to Buy and Sell Stock Easy Topics Companies
# You are given an array of prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

# Example 1:

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
# Example 2:

# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
 

# Constraints:

# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104
import os
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        best_price = 0
        best_day = 0
        for price in prices:
            max_diff = max(prices[i:])
            current_sum = max_diff - price
            if current_sum > best_price:
                best_price = current_sum
                best_day = prices.index(price) + 1
            i +=1
        return best_price if best_price > 0 else 0

if __name__ == "__main__":
 Solution.maxProfit(os.argv[1])

        
