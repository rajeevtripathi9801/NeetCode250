from typing import List

class Solution:
    def bubble_sort(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for counter in range(size - 1, 0, -1):
            for counter2 in range(0, counter):
                if nums[counter2] > nums[counter2 + 1]:
                    nums[counter2 + 1], nums[counter2] = nums[counter2], nums[counter2 + 1]

        return nums

if __name__=="__main__":
    obj = Solution()
    nums = [13, 36, 24, 52, 20, 9]
    print(obj.bubble_sort(nums))