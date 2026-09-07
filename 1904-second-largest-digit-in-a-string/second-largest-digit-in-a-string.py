class Solution:
    def secondHighest(self, s: str) -> int:
        num={"1","2","3",'4','5','6','7','8','9','0'}
        arr=[]
        for i in s:
            if i in num:
                arr.append(int(i))
        flag=0
        i,j=0,1
        print(arr)
        while j<len(arr):
            if arr[i]!=arr[j]:
                flag=1
                break
            j+=1
        if flag==0:
            return -1
        for i in range(len(arr)):
            small=i
            for j in range(i,len(arr)):
                if arr[j]<arr[small]:
                    small=j
            arr[i],arr[small]=arr[small],arr[i]
        out=[]
        out.append(arr[0])
        for i in arr:
            if len(out)==0:
                out.append(i)
            else:
                if out[-1]!=i:
                    out.append(i)
        return out[-2]
                    
             

        