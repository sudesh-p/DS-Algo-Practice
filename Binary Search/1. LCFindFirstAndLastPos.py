# TC: O(lgN) - 2 LogN Functions
# SC: O(1) No auxillary DS used
# Did it work on LC : Yes.
# Personal Difficulty while solving it: None

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        if len(nums)==0:
            return ans
        left = self.bs(nums, target-0.2)
        right = self.bs(nums, target+0.2)
        if (right-left == 0):
            return ans
        ans[0] = left
        ans[1] = right-1
        return ans

    def bs(self, nums, target):
        left = 0
        right = len(nums)-1
        while left<=right:
            mid = left + (right-left)//2
            if nums[mid]>target:
                right = mid-1
            elif nums[mid]<target:
                left = mid+1
        return left
    
    