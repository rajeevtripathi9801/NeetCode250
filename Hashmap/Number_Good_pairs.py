from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0 
        for counter1 in range(0, len(nums)):
            for counter2 in range(counter1 + 1, len(nums)):
                if nums[counter1] == nums[counter2]:
                    good_pairs += 1
        
        return good_pairs


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        seen = {}
        good_pairs = 0

        for current in nums:
            if current in seen:
                good_pairs += seen[current]
                seen[current] += 1
            else:
                seen[current] = 1

        return good_pairs

if __name__ == "__main__":
    solution = Solution()
    print(solution.numIdenticalPairs([1,2,3,1,1,3]))  # Output: 4
    print(solution.numIdenticalPairs([1,1,1,1]))      # Output: 6
    print(solution.numIdenticalPairs([1,2,3]))        # Output: 0