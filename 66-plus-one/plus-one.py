class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res=0
        for i in digits:
            res=(res*10)+i
        res+=1
        arr=[]
        while res>0:
            arr.append(res%10)
            res=res//10
        return arr[::-1]
        
        