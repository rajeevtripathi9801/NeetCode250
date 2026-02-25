from typing import List 

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        nums.sort()
        result = []

        for counter1 in range(0, len(nums) - 3):
            if counter1 > 0 and nums[counter1] == nums[counter1 - 1]:
                continue
            
            for counter2 in range(counter1 + 1, len(nums) - 2):
                if counter2 > counter1 + 1 and nums[counter2] == nums[counter2 - 1]:
                    continue
                
                left = counter2 + 1 
                right = len(nums) - 1 

                while left < right:
                    total = nums[counter1] + nums[counter2] + nums[left] + nums[right]

                    if total == target:
                        result.append([
                            nums[counter1], 
                            nums[counter2], 
                            nums[left],
                            nums[right]
                        ])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    
                    elif total < target:
                        left+= 1 
                    else:
                        right-= 1
        
        return result

if __name__ == "__main__":
    obj = Solution()
    nums = [1,0,-1,0,-2,2]
    target = 0 
    answer = obj.fourSum(nums, target)

    print(answer)