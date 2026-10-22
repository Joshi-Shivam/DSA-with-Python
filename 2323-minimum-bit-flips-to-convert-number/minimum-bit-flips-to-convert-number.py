class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        a1=[]
        a2=[]
        while start>0:
            a1.append(start%2)
            start=start//2
        while goal>0:
            a2.append(goal%2)
            goal=goal//2
        a1=a1[::-1]
        a2=a2[::-1]
        if len(a1)>len(a2):
            temp=len(a1)-len(a2)
            for i in range(temp):
                a2.insert(i,0)
        elif len(a2)>len(a1):
            temp=len(a2)-len(a1)
            for i in range(temp):
                a1.insert(i,0)
        i,j=0,0
        count=0
        while j<len(a1):
            if a1[i]!=a2[j]:
                count+=1
            i+=1
            j+=1
        return count
        
                        
                
        