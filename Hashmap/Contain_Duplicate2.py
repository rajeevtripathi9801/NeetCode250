from typing import List

# class Solution:
#     def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
#         for i in range(len(nums)):
#             for j in range(i + 1, min(i + k + 1, len(nums))):
#                 if nums[i] == nums[j]:
#                     return True
#         return False
    
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = set()

        for i, num in enumerate(nums):
            if num in seen:
                return True
 
            seen.add(num)

            if len(seen) > k:
                seen.remove(nums[i - k])

        return False
