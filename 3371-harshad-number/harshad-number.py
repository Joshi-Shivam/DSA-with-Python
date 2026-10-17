class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        res=0
        temp=x
        while x:
            res+=x%10
            x=x//10
        if temp%res==0:
            return res
        else:
            return -1



        