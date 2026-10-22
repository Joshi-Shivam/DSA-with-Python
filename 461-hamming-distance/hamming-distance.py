class Solution:
    def hammingDistance(self, x: int, y: int) -> int:        
        a1=[]
        a2=[]
        while x>0:
            a1.append(x%2)
            x=x//2
        while y>0:
            a2.append(y%2)
            y=y//2
        a1=a1[::-1]
        a2=a2[::-1]
        print(a1,a2)
        if len(a2)>len(a1):
            temp=len(a2)-len(a1)
            for i in range(temp):
                a1.insert(i,0)
        elif len(a1)>len(a2):
            temp=len(a1)-len(a2)
            for i in range(temp):
                a2.insert(i,0)
        i,j=0,0
        count=0
        while j<len(a1):
            if a1[i]!=a2[j]:
                count+=1
            i+=1
            j+=1
        return count
        