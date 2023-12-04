class OrderedStream:

    def __init__(self, n: int):
        self.os = [None]*n
        self.ptr = 0
        return None

    def insert(self, idKey: int, value: str) -> List[str]:
        cur = self.os
        p = self.ptr
        k = self.ptr
        cur[idKey-1] = value
        # print("Before",cur,p)
        while p<len(cur) and cur[p]:
            p += 1
            # print("In",cur,p)
        # print("After",cur,p)
        self.ptr = p
        self.os = cur
        return self.os[k:p]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)