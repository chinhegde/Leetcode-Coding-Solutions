# https://leetcode.com/problems/remove-letter-to-equalize-frequency/
# 2423. Remove Letter To Equalize Frequency
from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        counts = Counter(word)

        for key in counts.copy():
            counts[key] -= 1

            if counts[key] == 0:
                del counts[key]

            if len(set(counts.values())) == 1:
                return True
            
            counts[key] += 1

        return False