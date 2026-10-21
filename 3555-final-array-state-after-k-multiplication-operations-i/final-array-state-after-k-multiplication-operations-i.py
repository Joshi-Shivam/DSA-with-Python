class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        count=0
        while count<k:                
            idx=0
            for i in range(len(nums)):
                if nums[i]<nums[idx]:
                    idx=i
            
            nums[idx]=nums[idx]*multiplier
            count+=1
        return nums


            
        