class Solution:
    def mostWordsFound(self, sen: List[str]) -> int:
        return max([len(i.split(' ')) for i in sen])