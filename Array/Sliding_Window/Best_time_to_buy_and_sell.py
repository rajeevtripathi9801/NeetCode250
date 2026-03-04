from typing import List
class Solution:
    """
    Time complexity: O(n^2) where n is the size of the array
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        max_profit = 0
        profit = -1000000
        for buying_day in range(0, size - 1):
            for selling_day in range(buying_day + 1, size):
                profit = prices[selling_day] - prices[buying_day]

                if profit > max_profit:
                    max_profit = profit
        return max_profit
    """

    # Time Comlexity - O(n) where n is size of the array
    def maxProfit(self, prices: List[int]) -> int:
        buying, selling = 0, 1
        max_profit = 0
        size = len(prices)

        while selling < size:
            if prices[buying] < prices[selling]:
                profit = prices[selling] - prices[buying]
                max_profit = max(max_profit, profit)

            else:
                buying = selling

            selling += 1

        return max_profit

if __name__ == "__main__":
    sol = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    result = Solution().maxProfit(prices)
    print(result)
