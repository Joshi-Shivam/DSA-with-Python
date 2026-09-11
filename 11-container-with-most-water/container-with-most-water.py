class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max=0
        while l<r:
            if height[l]<height[r]:
                if height[l]*(r-l)>max:
                    print(f"Max change when {height[l]} and {height[r]}")
                    max=height[l]*(r-l)
                    print(f"current max {max}")
                l+=1
            else:
                if height[r]*(r-l)>max:
                    print(f"Max change when {height[l]} and {height[r]}")
                    max=height[r]*(r-l)
                    print(f"current max {max}")
                r-=1
            
        return max

        