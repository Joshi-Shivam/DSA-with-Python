class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count=0
        for i in nums:
            new=""
            while i>0:
                ld=i%10
                new+=str(ld)
                i=i//10
            if len(new)%2==0:
                count+=1
        return count
        