class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        h1={}
        h2={}
        for i in nums1:
            if i in h1:
                h1[i]+=1
            else:
                h1[i]=1
        for i in nums2:
            if i in h2:
                h2[i]+=1
            else:
                h2[i]=1
        for i in h2.keys():
            if i in h1.keys():
                return i
        return -1
        
        