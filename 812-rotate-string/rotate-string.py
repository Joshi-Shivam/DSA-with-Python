class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        a1=[]
        a2=[]
        for i in s:
            a1.append(i)
        for j in goal:
            a2.append(j)
        print(a1,a2)
        i=0
        while i<len(a1):
            if a1==a2:
                return True
            else:
                x=a1.pop(0)
                a1.append(x)
            i+=1
        return False
        