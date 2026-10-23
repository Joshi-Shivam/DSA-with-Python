class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=0
        j=0
        res=""
        while i<len(word1) and j<len(word2):
            res+=word1[i]
            res+=word2[j]
            i+=1
            j+=1
        if i>=len(word1):
            for k in range(j,len(word2)):
                res+=word2[k]
        else:
            for k in range(i,len(word1)):
                res+=word1[k]
        return res