class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        possible_start = []
        for num in nums:
            if num-1 not in set_nums:
                possible_start.append(num)
        
        max_len = 0
        for poss in possible_start:
            i = poss
            l = 0
            while i in set_nums:
                l += 1
                i += 1
            max_len = max(max_len, l)
        
        return max_len