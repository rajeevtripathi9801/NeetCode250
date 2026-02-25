from typing import List 

# Time Complexity - O(N)
# Space Complexity - O(1)"h","e","l","l","o"]
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left_pointer = 0 
        right_pointer = len(s) - 1

        while left_pointer<= right_pointer:
            s[left_pointer], s[right_pointer] = s[right_pointer], s[left_pointer]
            left_pointer +=1 
            right_pointer -=1

        return s
    
# Another Approach is to be done in stack 
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        stack = []
        for c in s:
            stack.append(c)
        i = 0
        while stack:
            s[i] = stack.pop()
            i += 1
            
if __name__ == "__main__":
    obj = Solution()
    s = ["h","e","l","l","o"]
    print(obj.reverseString(s))