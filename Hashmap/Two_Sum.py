from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for counter in range(0, len(nums)):
            for counter2 in range(counter + 1, len(nums)):
                if nums[counter] + nums[counter2] == target:
                    return [counter, counter2]


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         found = {}
#         result = []
#
#         for counter in range(0, len(nums)):
#             required = target - nums[counter]
#
#             if required in found:
#                 result = [found[required], counter]
#
#             found[nums[counter]] = counter
#
#         return result

if __name__ == '__main__':
    nums = [2,11,15, 7]
    target = 22
    solution = Solution()
    print(solution.twoSum(nums, target))