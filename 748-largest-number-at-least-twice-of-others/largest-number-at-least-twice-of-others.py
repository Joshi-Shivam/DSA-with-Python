class Solution:
    def dominantIndex(self, nums: list[int]) -> int:
        og={}
        for i in range(len(nums)):
            og[nums[i]]=i
        nums.sort()
        hash={}
        for i in range(len(nums)-1):
            hash[nums[i]]=nums[i]*2
        for i in hash:
            if hash[i]>nums[-1]:
                return -1
        for i in og:
            if i==nums[-1]:
                return og[i]

            
        