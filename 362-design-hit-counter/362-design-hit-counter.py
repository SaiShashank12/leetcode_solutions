class HitCounter:

    def __init__(self):
        self.hit_count=collections.deque()

    def hit(self, timestamp: int) -> None:
        self.hit_count.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        
        while self.hit_count and timestamp-self.hit_count[0]>=300:
            self.hit_count.popleft()
        return len(self.hit_count)
            
            
                


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)