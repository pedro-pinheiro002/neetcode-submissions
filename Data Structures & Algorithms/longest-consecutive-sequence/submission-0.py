class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        woutDupls = set(nums)
        longest = 0
        for num in woutDupls:
            if not num - 1 in woutDupls:
                i = 1
                while num+i in woutDupls:
                    i += 1
                longest = max(longest, i)
        return longest  

            
