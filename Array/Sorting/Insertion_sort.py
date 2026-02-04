from typing import List

class Solution:
    def insertion_sort(self, nums: List[int]) -> List[int]:
        size = len(nums)
        for counter in range(0, size):
            for counter2 in range(counter, 0, -1):
                if nums[counter2 - 1] > nums[counter2]:
                    nums[counter2 - 1], nums[counter2] = nums[counter2], nums[counter2 - 1]

        return nums

if __name__=="__main__":
    obj = Solution()
    nums = [13, 36, 24, 52, 20, 9]
    print(obj.insertion_sort(nums))