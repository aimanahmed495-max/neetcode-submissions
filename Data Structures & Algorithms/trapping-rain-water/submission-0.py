class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1

        water = 0

        maxL = height[l]
        maxR = height[r]

        while l < r :
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                water = water + maxL - height[l]
            else:
                r -= 1 
                maxR = max(maxR, height[r])
                water = water + maxR - height[r]
        return water
