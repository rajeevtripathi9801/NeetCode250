from typing import List 

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1 

        while left < right:
            if s[left] != s[right]:  
                """We will create substring skipping both the characters once 
                the left one and then right one then check which one creates 
                valid poalindrome if none then return FALSES
                ie aaaz as a and z are not equal then we create a substring
                removing to check when skipL then it becomes aaz and skipR becomes
                aaa which will be a palindrome 

                aaaz ---> aaz which needs to """
                
                skipL = s[left + 1: right + 1]
                skipR = s[left : right]

                return (skipL == skipL[::-1] or skipR == skipR[::-1])
            
            left+= 1
            right -= 1
        
        return True 

if __name__== "__main__":
    obj = Solution()
    s = "abc" 
    print(obj.validPalindrome(s))