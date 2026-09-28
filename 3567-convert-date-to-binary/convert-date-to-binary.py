class Solution:
    def convertDateToBinary(self, date: str) -> str:
        arr=[]
        n=""
        for i in date:
            if i=="-":
                arr.append(int(n))
                n=""
            else:
                n+=i
        arr.append(int(n))
        res=""
        for i in arr:
            temp=""
            while i>0:
                temp+=str(i%2)
                i=i//2
            res+=temp[::-1]
            res+="-"
        return res[0:-1]        


        