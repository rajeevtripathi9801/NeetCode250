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

if __name__ == '__main__':
    nums = [1,2,3,1]
    so = Solution()
    res = so.containsDuplicate(nums)
    print(res)