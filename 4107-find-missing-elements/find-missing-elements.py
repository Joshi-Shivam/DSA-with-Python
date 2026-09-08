class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            small=i
            for j in range(i,len(nums)):
                if nums[j]<nums[small]:
                    small=j
            nums[i],nums[small]=nums[small],nums[i]
        temp=[]
        for i in range(nums[0],nums[-1]+1):
            if i not in nums:
                temp.append(i)
        return temp
            
        