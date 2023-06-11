class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        hmap = []
        for i in s:
            if i not in hmap:
                hmap.append(i)
            else:
                hmap.remove(i)
                count += 2
        if len(hmap) != 0:
            count+=1
        return count