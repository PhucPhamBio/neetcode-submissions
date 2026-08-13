from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqCount = Counter(nums)
        return heapq.nlargest(k, freqCount.keys(), key = freqCount.get)