from typing import List

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_map = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for char in text:
            if char in balloon_map:
                balloon_map[char] += 1

        balloon_map['l'] //= 2      # 'l' appears twice in "balloon"
        balloon_map['o'] //= 2      # 'o' appears twice in "balloon"

        return min(balloon_map.values())
    
if __name__ == "__main__":
    solution = Solution()
    print(solution.maxNumberOfBalloons("nlaebolko"))  # Output: 1
    print(solution.maxNumberOfBalloons("loonbalxballpoon"))  # Output: 2
    print(solution.maxNumberOfBalloons("leetcode"))  # Output: 0