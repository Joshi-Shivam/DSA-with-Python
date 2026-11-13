class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for j,i in enumerate(nums,start=0):
            if i==target:
                return j
        return -1

