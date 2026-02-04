from typing import List 

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        size = len(nums) 
        count_of_required_subarrays = 0
        for counter1 in range(0, size):
            sum = 0
            for counter2 in range(counter1, size):
                sum = sum + nums[counter2]
                if sum == k:
                    count_of_required_subarrays += 1
        
        return count_of_required_subarrays


from collections import defaultdict

""" To optimize the soution use the a dictionary and prefix sum. 

Like [1, 2, 3] k = 3

prefix_count = 
At num = 1, prefix_count = {0 at 1 }
num = 2, prefix count 8 """
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1  # one way to have sum 0 before starting

        current_sum = 0
        subarray_count = 0

        for value in nums:
            current_sum += value

            required_sum = current_sum - k
            if required_sum in prefix_sum_count:
                subarray_count += prefix_sum_count[required_sum]

            prefix_sum_count[current_sum] += 1

        return subarray_count

if __name__ == "__main__":
    obj = Solution()
    nums = [1, 1, 1]
    k = 2
    print(obj.subarraySum(nums, k))