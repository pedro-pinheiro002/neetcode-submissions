class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        def prod(arr: List[int]) -> int:
            res = 1
            for num in arr:
                res *= num
            return res
        out = []
        for i in range(len(nums)):
            out.append(prod(nums[:i]) * prod(nums[i+1:]))
        return out