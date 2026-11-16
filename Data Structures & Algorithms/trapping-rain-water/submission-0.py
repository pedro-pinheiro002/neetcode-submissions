class Solution:
    def trap(self, height: List[int]) -> int:        
        prefix = []
        sufix = [0]*len(height)
        for i in range(len(height)):
            if i == 0:
                prefix.append(0)
                continue
            if height[i-1] > prefix[i-1]:
                prefix.append(height[i-1])
            else:
                prefix.append(prefix[i-1])
        
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                continue
            if height[i + 1] > sufix[i + 1]:
                sufix[i] = height[i+1]
            else:
                sufix[i] = sufix[i+1]
        print(prefix)
        print(sufix)
        res = 0
        for i in range(len(height)):
            water =  min(sufix[i], prefix[i]) - height[i]
            res += water if water > 0 else 0
        return res

            