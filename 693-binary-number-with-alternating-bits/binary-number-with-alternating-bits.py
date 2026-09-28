class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        res=[]
        while n>0:
            res.append(n%2)
            n=n//2
        print(res)
        i=0
        j=1
        while j<len(res):
            if res[i]==res[j]:
                return False
            i+=1
            j+=1
        return True
            

        