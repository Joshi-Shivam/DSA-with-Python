class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        n=len(nums)
        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        for i in dic.keys():
            if dic[i]>=n/2:
                return i
        