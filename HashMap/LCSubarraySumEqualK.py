class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hmap = {0:1} #Initial Case to take care of first subarray eg k=7 and we need [3,4]
        rsum = 0
        ans = 0
        for i in range(len(nums)):
            rsum = rsum+nums[i]
            if rsum-k in hmap:
                ans += hmap[rsum-k]
            
            if rsum in hmap:
                hmap[rsum] += 1
            else:
                hmap[rsum] = 1
        
        return ans