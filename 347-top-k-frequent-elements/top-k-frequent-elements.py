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
        for i in range(len(arr)):
            smal=i
            for j in range(i,len(arr)):
                if arr[j]>arr[smal]:
                    smal=j
            arr[i],arr[smal]=arr[smal],arr[i]
        new=[]
        count=0
        for i in arr:
            if len(new)==k:
                break
            for j in hash.keys():
                print(i,hash[j])
                if i==hash[j]:
                    if j not in new:
                        new.append(j)
        return new
        