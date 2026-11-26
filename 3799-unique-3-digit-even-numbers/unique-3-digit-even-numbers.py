class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        hash={}
        for i in digits:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1 
        res=0
        for i in range(100,1000,2):
            seth=hash.copy()
            temp=i
            flag=1
            while i>0:
                if (i%10) in seth and (seth[i%10]>=1):
                    seth[i%10]-=1
                    flag=1
                else:
                    flag=0
                    break
                i=i//10
            if flag==1:
                res+=1
        return res


        