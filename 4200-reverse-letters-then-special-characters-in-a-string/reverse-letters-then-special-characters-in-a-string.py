class Solution:
    def reverseByType(self, s: str) -> str:
        arr=[]
        for i in s:
            arr.append(i)
        i=0
        j=len(s)-1
        while i<j:
            if arr[i].isalpha():
                if arr[j].isalpha():
                    arr[i],arr[j]=arr[j],arr[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            elif arr[j].isalpha():
                if arr[i].isalpha():
                    arr[i],arr[j]=arr[j],arr[i]
                    i+=1
                    j-=1
                else:
                    i+=1
            else:
                i+=1
                j-=1
        print(arr)

        i+=1
        j-=1
        print(arr)
        i=0
        j=len(s)-1
        while i<j:
            if ord(arr[i]) not in range(65,91) and ord(arr[i]) not in range(97,123):
                if ord(arr[j]) not in range(65,91) and ord(arr[j]) not in range(97,123):
                    arr[i],arr[j]=arr[j],arr[i]
                    i+=1
                    j-=1
                else:
                    j-=1
            elif ord(arr[j]) not in range(65,91) and ord(arr[j]) not in range(97,123):
                if ord(arr[i]) not in range(65,91) and ord(arr[i]) not in range(97,123):
                    arr[i],arr[j]=arr[j],arr[i]
                    i+=1
                    j-=1
                else:
                    i+=1
            else:
                i+=1
                j-=1
            
        print(arr)
            
        res=""
        for i in arr:
            res+=i
        return res

        