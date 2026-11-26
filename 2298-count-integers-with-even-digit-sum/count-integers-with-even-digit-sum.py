class Solution:
    def countEven(self, num: int) -> int:
        arr=[]
        temp=[]
        for i in range(1,num+1):
            if i<=9:
                if i%2==0:
                    arr.append(i)
            else:
                temp=[]
                new=i
                while i>0:
                    temp.append(i%10)
                    i=i//10
                if sum(temp)%2==0:
                    arr.append(new)
        return len(arr)

        