class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        return None

    def add(self, val: int) -> int:
        arr = self.nums
        arr.append(val)
        arr = sorted(arr)
        self.nums = arr
        return arr[-self.k]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)