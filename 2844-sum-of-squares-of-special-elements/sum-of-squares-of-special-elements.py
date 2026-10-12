class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=0
        new=[]
        for j,i in enumerate(nums,start=1):
            if len(nums)%j==0:
                new.append(i)
        i=0
        while i<len(new):
            
            print(new)
            new[i]=new[i]*new[i]
            i+=1
        return sum(new)
        