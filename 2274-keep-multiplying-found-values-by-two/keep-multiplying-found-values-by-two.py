class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        hash={}
        for i in nums:
            hash[i]=1
        while original in hash:
            original*=2
        return original

        