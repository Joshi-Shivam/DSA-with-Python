class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        n=str(n)
        num=""
        for i in n:
            if i!="0":
                num+=i
        out=0
        for i in num:
            out+=int(i)
        return int(num)*out



        