class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        temp=[]
        i=0
        while i<len(arr2):
            if arr2[i] in arr1:
                x=arr1.pop(arr1.index(arr2[i]))
                temp.append(x)
            else:
                i+=1
        arr1.sort()
        for i in arr1:
            temp.append(i)
        return temp


        