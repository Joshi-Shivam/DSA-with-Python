class Solution:
    def findClosestNumber(self, nums: list[int]) -> int:
        has={"min":None}
        smol=float("inf")
        for i in nums:          
            if i<0:
                temp=i*-1
                if temp<smol:
                    smol=temp
                    has["min"]=-smol
            else:
                if i<=smol:
                    smol=i
                    has["min"]=smol
        return has["min"]

        