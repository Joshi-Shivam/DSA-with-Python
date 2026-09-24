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
            print(hash)
            for i in hash.values():
                temp.append(i)
            for i in range(len(temp)):
                small=i
                for j in range(i,len(temp)):
                    if temp[j]<temp[small]:
                        small=j
                temp[i],temp[small]=temp[small],temp[i]
            print(temp)
            max=temp[-1]
            if max==0:
                max=1
            print(max)
            for i in hash:
                if hash[i]==max:
                    arr.append(i)
        arr.sort()
        return arr


        