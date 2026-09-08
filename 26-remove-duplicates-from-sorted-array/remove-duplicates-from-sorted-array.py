class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        r=1
        count=1
        while r<=len(nums)-1:
            if nums[l]!=nums[r]:
                l+=1
                nums[l],nums[r]=nums[r],nums[l]
                count+=1
                r+=1
            else:
                r+=1
        return count
