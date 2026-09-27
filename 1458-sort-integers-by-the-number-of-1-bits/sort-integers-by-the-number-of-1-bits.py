class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        hash={}
        arr.sort()
        for i in arr:
            n=i
            temp=0
            while i>0:
                if i%2==1:
                    temp+=1
                i=i//2
            hash[n]=temp
        big=max(hash.values())
        res=[]
        for i in range(big+1):
            for j in arr:
                if hash[j]==i:
                    res.append(j)
        return res


        