class Solution:
    def countDistinctIntegers(self, nums: list[int]) -> int:
        hash={}
        for i in nums:
            temp=0
            hash[i]=0
            while i>0:
                temp=(temp*10)+(i%10)
                i=i//10
            if temp not in hash:
                hash[temp]=0
        return len(hash)


        