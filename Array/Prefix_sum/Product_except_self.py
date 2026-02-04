from typing import List 

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix_product = [0] * size
        suffix_product = [0] * size
        output = [0] * size

        prefix_product[0] = 1
        suffix_product[size - 1] = 1

        for counter in range(1, size):
            prefix_product[counter] = prefix_product[counter - 1] * nums[counter - 1]
        
        for counter in range(size -2, -1, -1):
            suffix_product[counter] = suffix_product[counter + 1] * nums[counter + 1]

        for counter in range(0, size):
            output[counter] = prefix_product[counter] * suffix_product[counter]
        
        return output


if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4]
    result = solution.productExceptSelf(nums)
    print(result)  # Output: [24, 12, 8, 6]