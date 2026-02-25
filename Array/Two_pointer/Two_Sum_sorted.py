from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_pointer = 0
        right_pointer = len(numbers) - 1
        sum = float("-inf")

        while left_pointer <= right_pointer:
            sum = numbers[left_pointer] + numbers[right_pointer]
            
            if sum > target:
                right_pointer -= 1
            elif sum == target:
                return [left_pointer + 1, right_pointer + 1]
            else:
                left_pointer += 1
        return []

if __name__ == "__main__":
    sol = Solution()
    numbers = [2,7,11,15]
    target = 9
    result = sol.twoSum(numbers, target)
    print(result)  # Output: [1, 2]