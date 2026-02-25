from typing import List 

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged_string = [] 

        idx_word1 = 0
        idx_word2 = 0 
        len_word1 = len(word1)
        len_word2 = len(word2)
        
        while idx_word1 < len_word1 or idx_word2 < len_word2:

            if idx_word1 < len_word1:
                merged_string.append(word1[idx_word1])
                idx_word1 += 1
            
            if idx_word2 < len_word2:
                merged_string.append(word2[idx_word2])
                idx_word2 += 1
        
        return "".join(merged_string)

if __name__ == "__main__":
    obj = Solution()
    s1 = "abc"
    s2 = "pqr"
    result = obj.mergeAlternately(s1, s2)
    print(result)
