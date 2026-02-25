from typing import List 

class Solution:
    def valindrome(self, s: str) -> bool:
        return s == s[::-1]


if __name__=="__main__":
    obj = Solution()
    name = "aaabaaa"
    result = obj.valindrome(name)
    print(result)