class Solution:
    def groupThePeople(self, gs: List[int]) -> List[List[int]]:
        groups = {}
        for i, size in enumerate(gs):
            if size not in groups:
                groups[size] = []
            groups[size].append(i)
            if len(groups[size]) == size:
                yield groups.pop(size)