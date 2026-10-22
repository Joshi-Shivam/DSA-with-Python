class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            small=i
            for j in range(i,len(nums)):
                if nums[j]<nums[small]:
                    small=j
            nums[i],nums[small]=nums[small],nums[i]
        arr=[]
        for i in range(len(nums)):
            if nums[i]==target:
                arr.append(i)
        return arr

        