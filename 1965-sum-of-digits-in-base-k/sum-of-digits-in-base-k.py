class Solution:
    def sumBase(self, n: int, k: int) -> int:
        arr=[]
        while n//k!=0:
            arr.append(n%k)
            n=n//k
        arr.append(n%k)
        return sum(arr)


        