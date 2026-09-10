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
        for i in range(len(arr1)):
            small=i
            for j in range(i,len(arr1)):
                if arr1[j]<arr1[small]:
                    small=j
            arr1[i],arr1[small]=arr1[small],arr1[i]
        for i in arr1:
            temp.append(i)
        return temp


        