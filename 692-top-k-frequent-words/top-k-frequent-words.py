class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        hash={}
        for i in words:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        arr=[]
        for i in hash.values():
            arr.append(i)
        arr.sort(reverse=True)
        res=[]
        for i in arr:
            small=None
            for j in hash.keys():
                if hash[j]==i:                    
                    if small is None or j<small:
                        small=j                        
            res.append(small)                    
            del hash[small]
        while k<len(res):
            x=res.pop(k)
        return res

        