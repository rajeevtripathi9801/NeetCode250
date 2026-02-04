# brute force 
# time complexity - O(N^2)
class Solution:

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
    
if __name__ == "__main__":
    nums = [7,1,5,3,6,4]
    obj = Solution()
    print(obj.maxProfit(nums))


# Single pass solution 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price 
            
            profit = price - min_price
            max_profit = max(profit, max_profit)
        
        return max_profit


# Two pointer solution 

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying, selling = 0, 1
        max_profit = 0
        size = len(prices)

        while selling < size:
            if prices[buying] < prices[selling]:
                profit = prices[selling] - prices[buying]
                max_profit = max(max_profit, profit)        
            else:
                buying = selling            # Move left pointer only when selling price is less than buying price
            
            selling += 1
        
        return max_profit