class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        water = 0
        lMax = height[0]
        rMax = height[len(height) - 1]
        while l < r:
            if height[l] < height[r]:
                l+=1
                lMax= max(lMax, height[l])
                water+= (lMax - height[l])
            else:
                r-=1
                rMax= max(rMax, height[r])
                water+= (rMax - height[r])
        return water
