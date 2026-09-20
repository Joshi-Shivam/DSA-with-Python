class Solution:
    def reverseDegree(self, s: str) -> int:
        hash={}
        st="abcdefghijklmnopqrstuvwxyz"
        j=0
        for i in range(26,0,-1):
            hash[st[j]]=i
            j+=1
        res=0
        count=1
        for i in range(len(s)):
            res+=hash[s[i]]*count
            count+=1
        return res


        