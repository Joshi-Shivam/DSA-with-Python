class Solution:
    def binaryGap(self, n: int) -> int:
        arr=[]
        while n>0:
            arr.append(n%2)
            n=n//2
        print(arr)
        res=[]
        i=0
        j=1
        for i in range(len(arr)):
            if arr[i]==1:
                for j in range(i+1,len(arr)):
                    if arr[j]==1:
                        res.append(j-i)
                        break
        if len(res)==0:
            return 0
        else:
            return max(res)

                    

        