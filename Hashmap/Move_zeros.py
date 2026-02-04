class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """ 
            Do not return anything, modify nums in-place instead.
        """
        left_pointer = 0 

        for counter in range(0, len(nums)):
            if nums[counter] != 0:
                nums[counter], nums[left_pointer] = nums[left_pointer],nums[counter]
                left_pointer += 1


# Time Complexity - O(N)
# Space Complexity - O(1) 