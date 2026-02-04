from typing import List 

# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums) 
#         found = set()
#         for counter in range(n):
#             for counter2 in range(counter + 1, n):
#                 for counter3 in range(counter2 + 1, n):
#                     if nums[counter] + nums[counter2] + nums[counter3] == 0:
#                         trip = tuple(sorted((nums[counter], nums[counter2], nums[counter3])))
#                         found.add(trip)
#         return [list(t) for t in found]

""" Just sort the array and then fix one point then it basically then it becomes Two sum 2 with the sorted array 
To return dont use a set as the element will be already and when coming in the the array. But it will have the 
duplicates so keep a looop to increase the folowing pointer if previous and current element are not same. 
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        sol = []
        nums.sort()

        for counter in range(0, size - 2):
            if counter > 0 and nums[counter] == nums[counter - 1]:
                continue
            
            left_pointer = counter + 1 
            right_pointer = size - 1
            
            while left_pointer < right_pointer:
                sum = nums[counter] + nums[left_pointer] + nums[right_pointer]
                if sum > 0:
                    right_pointer -= 1 
                    
                elif sum < 0:
                    left_pointer += 1
                
                else:
                    sol.append([nums[counter], nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    right_pointer -= 1

                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                        left_pointer += 1
                    while left_pointer < right_pointer and nums[right_pointer] == nums[right_pointer + 1]:
                        right_pointer -= 1

        return sol
    
if __name__=="__main__":
    sol = Solution()
    nums = [-1, 0, 1, 2, -1, 4]
    print(sol.threeSum(nums))
