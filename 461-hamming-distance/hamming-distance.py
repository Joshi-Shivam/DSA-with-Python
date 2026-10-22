class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        # if x==0 and y==0:
        #     return 0
        # if x==0 or y==0:
        #     if x==0:
        #         if y<10:
        #             return 1
        #         else:
        #             return 2
        #     elif y==0:
        #         if x<10:
        #             return 1
        #         else:
        #             return 2
        
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
            print("a2 len more")
            for i in range(temp):
                a1.insert(i,0)
        elif len(a1)>len(a2):
            temp=len(a1)-len(a2)
            print("a1 len more")
            for i in range(temp):
                a2.insert(i,0)
        print(a1,a2)
        i,j=0,0
        count=0
        while j<len(a1):
            try:
                if a1[i]!=a2[j]:
                    count+=1
            except IndexError:
                count+=1
            i+=1
            j+=1
        return count
        