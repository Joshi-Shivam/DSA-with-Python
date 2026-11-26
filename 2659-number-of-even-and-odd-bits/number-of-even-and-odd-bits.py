class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        arr=[]
        while n>0:
            arr.append(n%2)
            n=n//2
        i=0
        j=len(arr)-1
        while i<j:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
            j-=1
        even=0
        odd=0
        count=0
        for i in range(len(arr)-1,-1,-1):
            if arr[i]==1:
                if count%2==0:
                    even+=1
                else:
                    odd+=1
            count+=1
        return [even,odd]


        