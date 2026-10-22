class Solution:
    def countBits(self, n: int) -> list[int]:
        res=[]
        res.append(0)
        for i in range(1,n+1):
            arr=[]
            count=0
            while i>0:
                arr.append(i%2)
                i=i//2
            for i in arr:
                if i==1:
                    count+=1
            res.append(count)
        return res



        