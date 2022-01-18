class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.result=[]
        while v1 and v2:
            self.result.append(v1.pop(0))
            self.result.append(v2.pop(0))
        if v1:
            self.result.extend(v1)
        if v2:
            self.result.extend(v2)
            

    def next(self) -> int:
        return self.result.pop(0)
        

    def hasNext(self) -> bool:
        return len(self.result)!=0
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())