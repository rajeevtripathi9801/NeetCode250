# hashmap method 
from typing import List 

class Solution:
    def majority_element(self, nums: List[int]) -> int: 
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] +=1
            else:
                frequency[num] = 1
            
        for key, value in frequency.items():
            if value > 1:
                majority_element = key

        return majority_element

if __name__=="__main__":
    nums = [1,2,3, 2, 1, 2]
    obj = Solution()
    print (obj.majority_element(nums))

# Voting Algorithm 

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         size = len(nums)
        
#         counter = 0
#         current_max = -100000000
#         for counter1 in range(0, size):
#             if counter == 0:
#                 current_max = nums[counter1]
#                 counter = 1
#             elif counter != 0 and nums[counter1] != current_max:
#                 counter-= 1
#             else:
#                 counter+= 1

#         return current_max