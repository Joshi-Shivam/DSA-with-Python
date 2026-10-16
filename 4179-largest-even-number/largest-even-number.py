class Solution:
    def largestEven(self, s: str) -> str:
        if s[-1]=="2":
            return s
        else:
            flag=0
            for i in range(len(s)-1,-1,-1):
                if s[i]=="2":
                    flag=1
                    break
        if flag==0:
                return ""
        
        res=""
        for j in range(0,i+1):
            res+=s[j]
        return res

        