from typing import List

class Solution:
    def selection_sort(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for counter in range(size - 1):
            minimum_index = counter
            for counter2 in range(counter + 1, size):
                if nums[counter2] < nums[minimum_index]:
                    minimum_index = counter2
            nums[counter], nums[minimum_index] = nums[minimum_index], nums[counter]
        return nums

if __name__=="__main__":
    obj = Solution()
    nums = [13, 36, 24, 52, 20, 9]
    print(obj.selection_sort(nums))