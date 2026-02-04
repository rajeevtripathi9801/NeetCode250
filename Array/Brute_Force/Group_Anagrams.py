# from typing import List 

# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         groups = defaultdict(list)

#         for word in strs:
#             key = "".join(sorted(word))
#             groups[key].append(word)

#         result = list(groups.values())
#         return result
    
#defaultdict(<class 'list'>, {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']})



# Time Complexity - O(k logk * number of words in the array)
from typing import List 
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            count_array = [0] * 26

            for c in s:
        
        # Differnce of ASCII value of r and a should be the index at which it should be in the char frequency array
                count_array[ord(c) - ord('a')] += 1         
            
            result[tuple(count_array)].append(s)

        return result.values()

if __name__=="__main__":
    obj = Solution()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(obj.groupAnagrams(strs))


"""defaultdict ->, {(1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['eat', 'tea', 'ate'], 
(1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['tan', 'nat'], 
(1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']})
"""