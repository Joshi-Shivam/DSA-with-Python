class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        hash={}
        while n>0:
            if n%10 in hash:
                hash[n%10]+=1
            else:
                hash[n%10]=1
            n=n//10
        small=10
        print(hash)
        for i in hash.values():
            if i<small:
                small=i
        print(small)
        arr=[]
        for i in hash.keys():
            if hash[i]==small:
                arr.append(i)
        out=arr[0]
        for i in arr:
            if i<out:
                out=i
        return out
        