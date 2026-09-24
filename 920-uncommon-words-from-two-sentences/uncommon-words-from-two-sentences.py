class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
        hash={}
        res=""
        for i in s1:
            if i==" ":
                if res in hash:
                    hash[res]+=1
                else:
                    hash[res]=1
                res=""
            else:
                res+=i
        if res in hash:
                hash[res]+=1
        else:
                hash[res]=1
        hash2={}
        word=""
        for i in s2:
            if i==" ":
                if word in hash2:
                    hash2[word]+=1
                else:
                    hash2[word]=1
                word=""
            else:
                word+=i
        if word in hash2:
                hash2[word]+=1
        else:
                hash2[word]=1
        arr=[]
        for i in hash2:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=hash2[i]
        for i in hash:
            if hash[i]==1:
                arr.append(i)
        return arr
        

                
        
        

        