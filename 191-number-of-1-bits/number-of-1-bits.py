class Solution:
    def hammingWeight(self, n: int) -> int:
        bit=""
        while n>=1:
            bit+=str(n%2)
            n=n//2
        count=0
        for i in bit:
            if i=="1":
                count+=1
        return count