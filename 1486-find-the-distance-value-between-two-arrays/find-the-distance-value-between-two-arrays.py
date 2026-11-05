class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count=0
        for i in arr1:
            flag=0
            for j in arr2:
                temp=i-j
                if temp<0:
                    temp*=-1
                if temp <=d:
                    flag=1
                    break
            if flag==0:
                count+=1
        return count

