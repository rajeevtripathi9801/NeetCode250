from typing import List

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapST, mapTS = {}, {}

        for counter in range(len(s)):
            c1, c2 = s[counter], t[counter]

            if ((c1 in mapST and mapST[c1] != c2) 
                or (c2 in mapTS and mapTS[c2] != c1)):
                return False
            
            mapST[c1] = c2
            mapTS[c2] = c1
        
        return True

if __name__ == "__main__":
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))  # Output: True
    print(solution.isIsomorphic("foo", "bar"))  # Output: False
    print(solution.isIsomorphic("paper", "title"))  # Output: True