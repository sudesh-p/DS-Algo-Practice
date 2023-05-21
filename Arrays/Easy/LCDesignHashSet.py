NUM_BUCKETS = 37

class MyHashSet:

    def __init__(self):
        self.buckets = [[] for _ in range(NUM_BUCKETS)]
    
    def calc(self,key) -> int:
        return key % NUM_BUCKETS

    def add(self, key: int) -> None:
        mod = self.calc(key)
        if not key in self.buckets[mod]:
            self.buckets[mod].append(key)

    def remove(self, key: int) -> None:
        mod = self.calc(key)
        try:
            self.buckets[mod].remove(key)
        except:
            pass
           
    def contains(self, key: int) -> bool:
        mod = self.calc(key)
        return key in self.buckets[mod]