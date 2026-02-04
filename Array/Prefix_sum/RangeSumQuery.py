from  typing import List 

# class NumArray:

#     def __init__(self, nums: List[int]):
#         self.nums = nums

#     def sumRange(self, left: int, right: int) -> int:
#         sum = 0 
#         for current in range(left, right + 1):
#             sum += self.nums[current]
        
#         return sum 
    
class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        current_sum = 0

        for num in nums:
            current_sum += num
            self.prefix.append(current_sum)


    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix[right]
        if left > 0:
            left_sum = self.prefix[left - 1]
        else:
            left_sum = 0

        return right_sum - left_sum


if __name__ == "__main__":
    nums = [-2, 0, 3, -5, 2, -1]
    obj = NumArray(nums)

    print(obj.sumRange(0, 2))  # expected 1
    print(obj.sumRange(2, 5))  # expected -1
    print(obj.sumRange(0, 5))  # expected -3
