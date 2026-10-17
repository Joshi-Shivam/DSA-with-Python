class Solution:
    def divideArray(self, nums: list[int]) -> bool:
        if len(nums)%2!=0:
            return False
        else:
            hash={}
            for i in nums:
                if i in hash:
                    hash[i]+=1
                else:
                    hash[i]=1            
            for i in hash.values():
                if i%2!=0:                    
                    return False
            return True
        