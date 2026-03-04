from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
                
        return False
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.increasingTriplet([1,2,3,4,5]))  # Output: True
    print(solution.increasingTriplet([5,4,3,2,1]))  # Output: False
    print(solution.increasingTriplet([2,1,5,0,4,6]))  # Output: True
