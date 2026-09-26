class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash={}
        for i in nums:
            if i in hash:
                hash[i]+=1
            else:
                hash[i]=1
        arr=[]
        for i in hash.values():
            arr.append(i)
        arr.sort(reverse=True)
        new=[]
        count=0
        for i in arr:
            if len(new)==k:
                break
            for j in hash.keys():
                if i==hash[j]:
                    if j not in new:
                        new.append(j)
        return new
        