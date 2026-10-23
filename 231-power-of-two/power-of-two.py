class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count=0
        while n>0:
            if count==2:
                return False
            else:
                if (n%2)==1:
                    count+=1
                n=n//2
        if count==1:
            return True
        else:
            return False
        