from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n + 2):
            found = False

            for num in nums:
                if num == i:
                    found = True
                    break

            if not found:
                return i
        return -1  
    
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        set_nums = set()

        for num in nums:
            set_nums.add(num)

        for i in range(1, len(nums) + 2):
            if i not in set_nums:
                return i
        return -1  
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.firstMissingPositive([1,2,0]))        # Output: 3
    print(solution.firstMissingPositive([3,4,-1,1]))     # Output: 2
    print(solution.firstMissingPositive([7,8,9,11,12]))  # Output: 1