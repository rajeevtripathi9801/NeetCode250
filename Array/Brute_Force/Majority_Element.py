from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Boyer–Moore (n/3 variant): find up to two candidates
        candidate1 = candidate2 = None
        count1 = count2 = 0

        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        threshold = len(nums) // 3

        for candidate in (candidate1, candidate2):
            if candidate is not None and nums.count(candidate) > threshold:
                result.append(candidate)

        return result

if __name__ =="__main__":
    obj = Solution()
    nums = [3, 2, 3]
    result = obj.majorityElement(nums)
    print(result)