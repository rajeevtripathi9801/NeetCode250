from typing import List 

# Time Complexity - O(N)
# Space Complexity - O(N)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
    
# Time Complexity - O(N)
# Space Complexity - O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right: 
            while left < right and not s[left].isalnum():
                left +=1
            
            while left < right and not s[right].isalnum():
                right -=1
            
            if s[left].lower() != s[right].lower():
                return False 

            left +=1 
            right -= 1
        
        return True

if __name__ == "__main__":
    obj = Solution()
    s = "race a car"
    result = obj.isPalindrome(s)
    print(result)