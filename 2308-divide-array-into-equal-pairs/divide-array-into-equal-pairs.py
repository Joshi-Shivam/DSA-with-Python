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
            flag=1
            for i in hash.values():
                if i%2!=0:
                    flag=0
                    return False
            if flag==1:
                return True
            elif flag==0:
                return False
        