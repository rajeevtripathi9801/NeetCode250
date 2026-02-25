from typing import List 

class Solution:
    def sortColors(self, nums: List[int]) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        left_pointer = 0
        right_pointer = len(nums) - 1

        while counter <= right_pointer:
            if nums[counter] == 0:
                nums[counter], nums[left_pointer] = nums[left_pointer], nums[counter]
                left_pointer += 1
                counter += 1
            elif nums[counter] == 1:
                counter += 1
            else:
                nums[counter], nums[right_pointer] = nums[right_pointer], nums[counter]
                right_pointer -= 1

        return nums 

if __name__=="__main__":
    obj = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    print(obj.sortColors(nums))
    