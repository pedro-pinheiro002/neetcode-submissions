class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1]*n
        sufix_prod = [1]*n

        prefix_prod[0] = 1
        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]
        
        for j in range(n - 2, -1, -1):
            sufix_prod[j] = sufix_prod[j+1] * nums[j+1]

        return [prefix_prod[i]*sufix_prod[i] for i in range(n)]
