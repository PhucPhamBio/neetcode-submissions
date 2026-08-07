from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        value  = heapq.nlargest(k, counts.keys(), key = counts.get)
        return value