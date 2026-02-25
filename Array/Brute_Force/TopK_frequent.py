from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:  
        """Time complexity - O(n) + O(m) + O(mlogm) + O(k)
        When all are unique then m = n making TC = O(nlogn)
        n -> number of elements
        m -> no of unique elements in array
        k -> required top elements"""
        
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        # Example after this step:
        # nums = [1,1,1,2,2,3]
        # freq = {1: 3, 2: 2, 3: 1}

        # Step 2: Convert the frequency map into a list of pairs
        # We create (frequency, number) tuples instead of (number, frequency)
        # because Python sorts tuples from left to right,
        # and we want to sort primarily by frequency.
        pairs = []
        for num in freq:
            pairs.append((freq[num], num))

        # Example:
        # pairs = [(3, 1), (2, 2), (1, 3)]

        # Step 3: Sort the list in descending order
        # reverse=True means highest frequency comes first
        # Tuple sorting rules:
        #   - compare first element (frequency)
        #   - if tied, compare second element (number)
        pairs.sort(reverse=True)

        # After sorting:
        # pairs = [(3, 1), (2, 2), (1, 3)]

        # Step 4: Extract the top k numbers
        # Each item in pairs is (frequency, number)
        # pairs[i][1] gives us the number
        result = []
        for i in range(k):
            result.append(pairs[i][1])

        # If k = 2:
        # result = [1, 2]

        return result


if __name__ =="__main__":
    obj = Solution()
    nums = [1, 1, 1, 2, 3, 4, 2, 2]
    k = 2
    result = obj.topKFrequent(nums, k)

    print(result)