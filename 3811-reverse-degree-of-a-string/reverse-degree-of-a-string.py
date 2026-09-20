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
            print(f"current str {s[i]}")
            print(f"Hash value {hash[s[i]]} times i {count}")
            res+=hash[s[i]]*count
            print(f"Current res {res}")
            count+=1
        return res


        