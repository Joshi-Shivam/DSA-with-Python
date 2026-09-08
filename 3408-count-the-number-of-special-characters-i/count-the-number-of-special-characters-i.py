class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        new=""
        word=set(word)
        for i in word:
            if ord(i) in range(65,91):
                new+=chr(ord(i)+32)
            else:
                new+=i
        hash={}
        for i in new:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        res=0
        for i in hash.keys():
            if hash[i]>=2:
                res+=1
        return res

        