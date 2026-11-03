class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count=0
        nums.sort()
        for i in range(len(nums)):
            if nums[i]<nums[-1]:
                count=count+(nums[-1] -nums[i])
        return count


                    
        