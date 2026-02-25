from typing import List

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        n = len(nums) 
        count = 0 
        for counter in range(0, n):
            counter2 = counter

            while counter2<n and nums[counter2] == 0:
                count+= 1
                counter2+= 1
        
        return count
    
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res, count = 0, 0

        for num in nums:
            if num == 0:
                count+= 1
            else:
                count = 0 
            res = res + count

        return res            

if __name__ == "__main__":
    solution = Solution()
    print(solution.zeroFilledSubarray([1,3,0,0,2,0,0,4]))  # Output: 6
    print(solution.zeroFilledSubarray([0,0,0,2,0,0]))      # Output: 9
    print(solution.zeroFilledSubarray([2,10,2019]))        # Output: 0