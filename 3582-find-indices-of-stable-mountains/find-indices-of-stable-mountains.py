class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        arr=[]
        i=1
        while i<len(height):
            if height[i-1]>threshold:
                arr.append(i)
            i+=1
        return arr

        