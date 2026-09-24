class Solution:
    def countWords(self, words1: list[str], words2: list[str]) -> int:
        hash={}
        hash2={}
        for i in words1:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for i in words2:
            if i in hash2:
                hash2[i]+=1
            else:
                hash2[i]=1
        count=0
        for i in hash2:
            if i in hash:
                if hash[i]==1 and hash2[i]==1:
                    count+=1
        return count
                
        