class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            small=i
            for j in range(i,len(nums)):
                if nums[j]<nums[small]:
                    small=j
            nums[i],nums[small]=nums[small],nums[i]
        hash={}
        for i in nums:
            hash[i]=1
        for i in range(k,nums[-1]+k+1):
            if i not in hash:
                if i%k==0:
                    return i
        

        