class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        res=""
        i=0
        while i<len(s):
            if len(stack)==0:
                stack.append(s[i])
                
            else:
                if s[i]=="*":
                    stack.pop()
                else:
                    stack.append(s[i])
            i+=1
        for i in stack:
            res+=i
        return res
        