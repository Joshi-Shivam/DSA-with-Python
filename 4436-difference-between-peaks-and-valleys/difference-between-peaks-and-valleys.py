class Solution:
    def peakValleyDifference(self, nums: list[int]) -> int:
        peak=0
        val=0
        i=1
        while i<len(nums)-1:
            if nums[i]> nums[i-1] and nums[i]>nums[i+1]:
                peak+=nums[i]
            elif nums[i]<nums[i-1] and nums[i]<nums[i+1]:
                val+=nums[i]
            i+=1
        return peak-val

        