class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        res=[]
        sum=0
        for i in num:
            sum=(sum+i)*10
        sum=sum//10
        sum=sum+k
        sum=int(sum)
        while sum>0:
            res.append(sum%10)
            sum=sum//10
        return res[::-1]
            

        