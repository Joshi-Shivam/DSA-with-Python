class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        og={}
        for i in range(len(nums)):
            og[nums[i]]=i
        print(og)
        for i in range(len(nums)):
            small=i
            for j in range(i,len(nums)):
                if nums[j]<nums[small]:
                    small=j
            nums[i],nums[small]=nums[small],nums[i]
        hash={}
        for i in range(len(nums)-1):
            hash[nums[i]]=nums[i]*2
        print(hash)
        flag=1
        for i in hash:
            if hash[i]>nums[-1]:
                return -1
        for i in og:
            if i==nums[-1]:
                return og[i]

            
        