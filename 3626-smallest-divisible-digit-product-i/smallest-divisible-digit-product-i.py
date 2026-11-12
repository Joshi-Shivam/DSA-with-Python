class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,1000):
            temp=[]
            copy=i
            while i>0:
                temp.append(i%10)
                i=i//10
            mul=1
            for k in temp:
                mul*=k
            if mul%t==0:
                return copy

        