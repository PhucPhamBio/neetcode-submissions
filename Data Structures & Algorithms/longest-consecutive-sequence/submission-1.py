class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_sets = set(nums)
        longest  = 0
        for num in num_sets:
            if num - 1 in num_sets:
                continue 
            
            length = 1 
            curr   = num
            while curr + 1 in num_sets:
                length += 1
                curr   += 1
            longest = max(longest, length)
        
        return longest