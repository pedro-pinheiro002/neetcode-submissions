class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        maxVol = 0
        while l < r:
            maxVol = max(maxVol, self.findWaterVol(heights, l, r))

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxVol

    def findWaterVol(self, heights, i, j):
        return abs(j - i)*min(heights[i], heights[j])



    