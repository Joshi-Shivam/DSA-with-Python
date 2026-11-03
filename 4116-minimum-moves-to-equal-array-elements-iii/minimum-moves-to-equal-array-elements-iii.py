class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)):
            small=i
            for j in range(i,len(nums)):
                if nums[small]>nums[j]:
                    small=j
            nums[i],nums[small]=nums[small],nums[i]
        print(nums)
        for i in range(len(nums)):
            if nums[i]<nums[-1]:
                count=count+(nums[-1] -nums[i])
        return count


                    
        