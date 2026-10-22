class Solution:
    def smallestNumber(self, n: int) -> int:
        if n==1:
            return 1
        hash={3:None,7:None,15:None,31:None,63:None,127:None,255:None,511:None,1023:None,2047:None,	4095:None,8191:None,16383:None,32767:None}
        for i in hash:
            hash[i]=i-n
            if hash[i]<0:
                hash[i]=1000
        temp=10000000
        for i in hash:
            if hash[i]<temp:
                temp=hash[i]
        for i in hash:
            if hash[i]==temp:
                return i

        