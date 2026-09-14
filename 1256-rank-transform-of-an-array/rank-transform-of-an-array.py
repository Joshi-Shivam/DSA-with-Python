class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        res=[]
        for i in arr:
            res.append(i)
        arr.sort()
        hash={}
        temp=[]
        count=1
        for i in arr:
            if i not in hash:
                hash[i]=count
                count+=1
        for i in res:
            temp.append(hash[i])
        return temp
        

            
            
        