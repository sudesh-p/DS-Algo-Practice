# TC: O(1)
# SC: O(Sq.Root(N)) #Used Double Hashing and DS inside DS [Array in Array]
# Did it work on LC : Yes.
# Personal Difficulty while solving it: Revised concept of DS in DS and Double Hashing.

class MyHashMap:

    def __init__(self):
        self.buckets = [None for i in range(1000)]
        self.containsNull = None
        self.maxNum = None
    
    def prim_hash(self,key):
        return key % 1000
    
    def sec_hash(self,key):
        return key//1000

    def put(self, key: int, value: int) -> None:
        if key == None:
            self.containsNull = value
            return
        elif key == 1000000:
            self.maxNum = value
            return
        pkey = self.prim_hash(key)
        skey = self.sec_hash(key)
        if self.buckets[pkey]==None:
            self.buckets[pkey] = [None for _ in range(1000)]
            self.buckets[pkey][skey]=value
        else:
            self.buckets[pkey][skey]=value
        
    def get(self, key: int) -> int:
        if key == None:
            return self.containsNull if self.containsNull else -1
        elif key == 1000000:
            return self.maxNum if self.maxNum else -1
        pkey = self.prim_hash(key)
        skey = self.sec_hash(key)
        if self.buckets[pkey]==None:
            return -1
        else:
            if self.buckets[pkey][skey] != None:
                return self.buckets[pkey][skey]
            else:
                return -1
        

    def remove(self, key: int) -> None:
        if key == None:
            self.containsNull = None
        elif key == 1000000:
            self.maxNum = None
        pkey = self.prim_hash(key)
        if self.buckets[pkey]==None:
            return None
        else:
            self.buckets[pkey][self.sec_hash(key)] = None