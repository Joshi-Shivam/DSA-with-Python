class Solution:
    def averageValue(self, nums: list[int]) -> int:
        res=0
        count=0
        for i in nums:
            print(res,count)
            if i%3==0 and i%2==0:
                res+=i
                count+=1
        if res==0 or count==0:
            return 0
        else:
            return res//count
        