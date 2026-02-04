class Solution:
    def contain_duplicates(self, nums: List[int], k: int) -> bool:
        
        seen = set()
        for current in nums:
        