from typing import List 

class Solution:
    def maxArea(self, height: List[int]) -> int:
        length_of_container = len(height)
        max_area = float("-inf")

        for counter in range(0, length_of_container - 1):
            for counter2 in range(counter + 1, length_of_container):
                length = counter2 - counter
                breadth = min(height[counter], height[counter2])       
                current_area = length * breadth 

                if current_area > max_area: 
                    max_area = current_area
        
        return max_area


""" To make sure main thing it works we have to check that min left should be less than the right pointer 
cause if we make them equal then basically their is nothing to hold the water. 
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        length_of_container = len(height)
        max_area = 0

        left_pointer = 0
        right_pointer =  length_of_container - 1

        while left_pointer < right_pointer:
            length = right_pointer - left_pointer
            breadth = min(height[left_pointer], height[right_pointer])       
            
            current_area = length * breadth

            max_area = max(max_area, current_area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer+= 1
            else:
                right_pointer-= 1  

        return max_area
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxArea([1,8,6,2,5,4,8,3,7]))  # Output: 49
    print(sol.maxArea([1,1]))  # Output: 1