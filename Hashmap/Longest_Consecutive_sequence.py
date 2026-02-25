from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        maxlength = 0

        for num in nums:
            if (num - 1) not in numset:
                length = 0
                while (num + length) in numset:
                    length +=1
                maxlength = max(length, maxlength)
        
        return maxlength

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))  # Output: 4
    print(sol.longestConsecutive([0,3,7,2,5,8,4,6,0,1]))  # Output: 9