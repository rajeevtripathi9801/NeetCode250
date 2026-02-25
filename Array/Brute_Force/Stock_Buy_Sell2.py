from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        for counter in range(1, len(prices)):
            if prices[counter] > prices[counter - 1]:
                profit += prices[counter] - prices[counter - 1]
            
        return profit

if __name__=="__main__":
    obj = Solution()
    nums = [7, 1, 3, 6, 4]
    result = obj.maxProfit(nums)
    print(result)
