from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        hm = dict(Counter(nums))
        print(hm)
        hm = dict(sorted(hm.items(), key=lambda item: item[1], reverse = True))
        print(hm,list(hm)[:k])
        return list(hm)[:k]