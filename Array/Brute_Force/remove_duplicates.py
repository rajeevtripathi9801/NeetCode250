class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_position = 1

        for counter in range(1,len(nums)):
            if nums[counter]!= nums[counter - 1]:
                nums[unique_position] = nums[counter]
                unique_position += 1 
        
        return unique_position

# Time Complexity - O(N)
# Space Complexity - O(1)