class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        arr=[]
        hash={}
        for i in range(left,right+1):
            x=i
            var=0
            while i>0:
                num=i%10
                if num==0:
                    var=0
                    break
                else:        
                    if x%num==0:
                        var=(var*10)+num
                    else:
                        var=0
                        break
                i=i//10
            if var==0:
                pass
            else:
                var=str(var)
                hash[var[::-1]]=0
        for i in hash.keys():
            arr.append(int(i))
        return arr







        