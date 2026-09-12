class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
       hash={}
       p=paragraph.lower()
       word=""
       for i in p:
        if ord(i) not in range(97,123) and ord(i) not in range(65,91):
            if word==" " or word=="":
                continue
            if word in hash:
                hash[word]+=1
            else:
                hash[word]=1
            word=""
        else:
            word+=i
       if word in hash:
        hash[word]+=1
       else:
        hash[word]=1  
       for i in banned:
        if i not in hash:
            continue
        else:
            del hash[i]
       print(hash)
       arr=[]
       for i in hash.values():
        arr.append(i)
       arr.sort()
       print(arr) 
       for i in hash:
        if hash[i]==arr[-1]:
            return i
        
