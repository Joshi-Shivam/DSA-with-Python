class Solution:
    def findValidPair(self, s: str) -> str:
        res=""
        hash={}
        for i in s:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        print(hash)
        i=0
        j=1
        if len(hash)<=1:
            return ""
        while j<len(s):
            if (s[i]!=s[j]) and (int(s[j])==hash[s[j]] and int(s[i])==hash[s[i]]):
                res+=s[i]
                res+=s[j]
                return res
            i+=1
            j+=1
            
        return ""