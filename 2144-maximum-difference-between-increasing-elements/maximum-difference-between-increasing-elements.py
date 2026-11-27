class Solution:
    def maximumDifference(self, nums: list[int]) -> int:
        max=-1
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if j>i:
                    if nums[j]>nums[i]:
                        if (nums[j]-nums[i])>max:
                            max=nums[j]-nums[i]
        return max