class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i in nums:
            if i in dic:
                dic[i]+=+1
            else:
                dic[i]=1
        for j in dic.keys():
            if dic[j]>1:
                return True
        return False
                