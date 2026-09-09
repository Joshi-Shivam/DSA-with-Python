class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        arr=[]
        for i in nums:
            temp=[]
            while i>0:
                temp.append(i%10)
                i=i//10
            arr.append(sum(temp))
        for i in range(len(arr)):
            if i==arr[i]:
                return i
        return -1
            
        