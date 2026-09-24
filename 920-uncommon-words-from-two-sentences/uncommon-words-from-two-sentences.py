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
        print(hash,hash2)
        arr=[]
        for i in hash2:
            print(f"Current {i}")
            if i in hash:
                print("Alread +1")
                hash[i]+=1
            else:
                print("New word =1")
                hash[i]=hash2[i]
        print(hash)
        for i in hash:
            if hash[i]==1:
                arr.append(i)
        return arr
        

                
        
        

        