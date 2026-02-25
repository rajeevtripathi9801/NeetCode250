from typing import List 

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        result = 0
        l, r = 0, len(people) - 1

        while l <= r:
            remain = limit - people[r]
            r-= 1
            result+= 1

            if l<=r and remain >= people[l]:
                l+= 1
        
        return result

if __name__=="__main__":
    obj = Solution()
    nums = [1, 2]
    limit = 3
    result = obj.numRescueBoats(nums, limit)
    print(result)