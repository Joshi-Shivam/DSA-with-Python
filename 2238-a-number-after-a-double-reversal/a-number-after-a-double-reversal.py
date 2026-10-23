class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        temp=num
        if num<10:
            return True
        else:
            new=0
            res=0
            while num>0:
                new=(new*10)+(num%10)
                num=num//10
            while new>0:
                res=(res*10)+(new%10)
                new=new//10
            if res==temp:
                return True
            else:
                return False  
            
        