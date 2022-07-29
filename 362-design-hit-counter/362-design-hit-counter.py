class HitCounter:

    def __init__(self):
        self.hits = {}

    def hit(self, timestamp: int) -> None:
        if timestamp not in self.hits:
            self.hits[timestamp] = 1
        else:
            self.hits[timestamp] += 1

    def getHits(self, timestamp: int) -> int:
        print(self.hits)
        num_hits = 0
        start = timestamp - 300 
        end = timestamp

        for key, value in self.hits.items():
            if key > start and key <= end:
                num_hits += value
        return num_hits
            
                
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)