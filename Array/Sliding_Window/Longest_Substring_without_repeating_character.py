from typing import List

class Solution:
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for current in range(0, len(s)):
            present = set()
            for current2 in range(current, len(s)):
                if s[current2] in present:
                    break
                present.add(s[current2])

            res = max(res, len(present))
        
        return res 
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = set()
        left = 0
        res = 0
        for right in range(0, len(s)):
            while s[right] in window:
                window.remove(s[left])
                left+= 1
            window.add(s[right])
            res = max(res, right - left + 1)

        return res