class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s==0:
            return 0
        else:
            if n==1:
                if s>=10:
                    return -1  
                else:          
                    return s
            if n==2:
                out=[]
                for i in range(10,100):
                    temp=[]
                    new=i
                    while i>0:                                              
                        temp.append(i%10)
                        i=i//10
                    if sum(temp)==s:
                        out.append(new)
                if len(out)==0:
                    return -1
                else:
                    return out[-1]
            elif n==3:
                temp=[]
                out=[]
                for i in range(100,1000):
                    temp=[]
                    new=i
                    while i>0:                                              
                        temp.append(i%10)
                        i=i//10
                    if sum(temp)==s:
                        out.append(new)
                if len(out)==0:
                    return -1
                else:
                    return out[-1]
            elif n==4:
                temp=[]
                out=[]
                for i in range(1000,10000):
                    temp=[]
                    new=i
                    while i>0:                                              
                        temp.append(i%10)
                        i=i//10
                    if sum(temp)==s:
                        out.append(new)
                if len(out)==0:
                    return -1
                else:
                    return out[-1]
            if n==5:
                temp=[]
                out=[]
                for i in range(10000,100000):
                    temp=[]
                    new=i
                    while i>0:                                              
                        temp.append(i%10)
                        i=i//10
                    if sum(temp)==s:
                        out.append(new)
                if len(out)==0:
                    return -1
                else:
                    return out[-1]

                        


        