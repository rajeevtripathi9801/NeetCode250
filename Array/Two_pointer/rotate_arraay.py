# from typing import List

# class Solution:
#     def rotate_array(self, nums: List[int], k: int) -> List[int]:
#         size = len(nums)

#         new_array = [0] * size

#         for counter in range(0, size):
#             new_array[(counter + k) % size] = nums[counter]
        
#         for counter in range(0, size):
#             nums[counter] = new_array[counter]

#         return nums
    
# if __name__=="__main__":
#     nums = [1, 2, 3, 4, 5, 6, 7]
#     k = 3
#     obj = Solution()
#     print(obj.rotate_array(nums, k))



from typing import List

class Solution:
    def reverse_helper(self, nums: List[int], start: int, end: int):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    
    def rotate_array(self, nums: List[int], k: int) -> List[int]:
        size = len(nums)
        k = k % size

        self.reverse_helper(nums, 0, size - 1)
        self.reverse_helper(nums, 0, k - 1)
        self.reverse_helper(nums, k, size - 1)
    
        return nums
    
if __name__=="__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    obj = Solution()
    print(obj.rotate_array(nums, k))