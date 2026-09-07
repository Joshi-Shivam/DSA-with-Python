class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for j,i in enumerate(nums,start=0):
            res=target-i
            if res in hash:
                return [hash[res],j]
            else:
                hash[i]=j
        