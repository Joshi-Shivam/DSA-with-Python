class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hash={}
        new=[]
        for i in arr:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        for i in hash.keys():
            if hash[i]==1:
                new.append(i)
        if len(new)<k:
            return ""
        else:
            return new[k-1]
        
        