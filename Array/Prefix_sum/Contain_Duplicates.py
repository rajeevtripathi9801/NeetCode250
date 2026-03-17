from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency_map = {}
        status = False

        for num in nums:
            if num in frequency_map:
                frequency_map[num] += 1
            else:
                frequency_map[num] = 1

        for key, value in frequency_map.items():
            if value > 1:
                status = True

        return status

# from typing import List
#
# class Solution:
#     def containsDuplicate(self, nums: List[int]) -> bool:
#         seen = set()
#
#         for num in nums:
#             if num in seen:
#                 return True
#             seen.add(num)
#
#         return False
#
#
# if __name__ == "__main__":
#     nums = [1, 2, 3, 1]
#     so = Solution()
#     print(so.containsDuplicate(nums))

if __name__ == '__main__':
    nums = [1,2,3,1]
    so = Solution()
    res = so.containsDuplicate(nums)
    print(res)