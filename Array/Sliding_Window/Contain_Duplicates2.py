from typing import List

class Solution:
    """def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        n = len(nums)
        for counter in range(n):
            for counter2 in range(counter + 1, min(counter + k + 1, n)):
                if nums[counter] == nums[counter2]:
                    return True

        return False
    """

    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        left = 0

        for right in range(len(nums)):
            if right - left > k:
                window.remove(nums[left])
                left += 1
            if nums[right] in window:
                return True
            window.add(nums[right])

        return False

if __name__ == '__main__':
    nums = [1, 1, 2, 3, 4, 4, 5, 5, 6]
    k = 2
    res = Solution().containsNearbyDuplicate(nums, k)
    print(res)