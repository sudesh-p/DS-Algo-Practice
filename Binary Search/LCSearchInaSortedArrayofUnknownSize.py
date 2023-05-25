# TC: O(lgN) - 2 LogN Functions
# SC: O(1) No auxillary DS used
# Did it work on LC : Yes, used Mohit's account to test as it was a premium problem.
# Personal Difficulty while solving it: None

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        low = 0
        high = 500
        while reader.get(high)<target:
                low = high
                high = high * 2

        while low<=high:
            mid = (low+high)//2
            if reader.get(mid)==target:
                return mid
            elif reader.get(mid)<target:
                low = mid+1
            elif reader.get(mid)>target:
                high = mid-1
        return -1