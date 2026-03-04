"""
Bruute Force is just create all the 4
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0

        for current1 in range(0, len(s)):
            count, maxf = {}, 0
            for current2 in range(current1, len(s)):
                count[s[current2]] = 1 + count.get(s[current2], 0)
                maxf = max(maxf, count[s[current2]])

                if (current2 - current1 + 1) - maxf <= k:
                    result = max(result, current2 - current1 + 1)

        return result