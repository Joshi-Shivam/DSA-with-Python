class Solution:
    def dayOfYear(self, date: str) -> int:
        arr=[]
        temp=""
        for i in date:            
            if i=="-":
                arr.append(int(temp))
                temp=""
            else:
                temp+=i
        arr.append(int(temp))
        res=0
        if (arr[0]%4==0 and arr[0]%100!=0) or (arr[0]%400==0):
            days=[31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335, 366]
            if arr[1]==1:
                return arr[-1]
            else:
                res+=days[arr[1]-2]+arr[-1]
        else:
            days=[31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]
            if arr[1]==1:
                return arr[-1]
            else:
                res+=days[arr[1]-2]+arr[-1]
        return res
