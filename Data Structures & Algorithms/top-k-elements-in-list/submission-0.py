from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        
        top_k = [item for item, value in frequencies.most_common(k)]

        return top_k
