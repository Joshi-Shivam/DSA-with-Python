class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            small=i
            for j in range(i,len(nums)):
                if nums[j]<nums[small]:
                    small=j
            nums[i],nums[small]=nums[small],nums[i]
        stack=[]
        for i in nums:
            if len(stack)==0:
                stack.append(i)
            else:
                if stack[-1]!=i:                    
                    stack.append(i)
        if len(stack)>=3:
            return stack[-3]
        else:
            if len(stack)==2:
                return stack[-1]
            else:
                return stack[-1]

        

        