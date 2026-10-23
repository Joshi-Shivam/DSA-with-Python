class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        res=""
        while n>=1:
            res+=str(n%2)
            n=n//2
        count=0
        for i in res:
            if count==2:
                return False
            else:
                if i=="1":
                    count+=1
        if count==1:
            return True
        else:
            return False
        