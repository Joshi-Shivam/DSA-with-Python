class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        arr=[]
        hash={}
        if len(nums)==1:
            for i in nums:
                for j in i:
                    arr.append(j)
        else:
            for i in nums:
                for j in i:
                    if j in hash:
                        hash[j]+=1
                    else:
                        hash[j]=0
            temp=[]
            for i in hash.values():
                temp.append(i)
            temp.sort()
            max=temp[-1]
            if max==0:
                max=1
            for i in hash:
                if hash[i]==max:
                    arr.append(i)
        arr.sort()
        return arr


        