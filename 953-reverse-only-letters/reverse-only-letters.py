class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr=[]
        for i in s:
            arr.append(i)
        i=0
        j=len(arr)-1
        while i<j:
            if ord(arr[i]) not in range(65,91) and ord(arr[i]) not in range(97,123):
                i+=1
            elif ord(arr[j]) not in range(65,91) and ord(arr[j]) not in range(97,123):
                j-=1
            else:
                arr[i],arr[j]=arr[j],arr[i]
                i+=1
                j-=1
        res=""
        for i in arr:
            res+=i
        return res

        