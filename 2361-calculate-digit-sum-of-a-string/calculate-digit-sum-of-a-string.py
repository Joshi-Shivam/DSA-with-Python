class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s)>k:
            arr=[]
            count=0
            temp=""
            for i in s:
                if count==0:
                    temp+=i
                    count+=1
                else:
                    if count%k==0:
                        arr.append(int(temp))
                        temp=""
                        temp+=i
                        count+=1
                    else:
                        temp+=i
                        count+=1
            arr.append(int(temp))
            res=""
            for i in arr:
                num=0
                if i==0:
                    res+="0"
                else:
                    while i>0:
                        num+=i%10
                        i=i//10
                    res+=str(num)
            s=res
        return s





        