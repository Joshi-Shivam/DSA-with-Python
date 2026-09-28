class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        res=0
        prime={2,3,5,7,11,13,17,19,23,29,31,37,41,43,47}
        for i in range(left,right+1):
            temp=0
            while i>0:
                if i%2==1:
                    temp+=1
                i=i//2
            if temp in prime:
                res+=1
        return res


        
        