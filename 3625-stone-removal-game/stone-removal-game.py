class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n==10:
            return True
        place=0
        turn=10
        flag=None
        while n>0:
            if (n-turn)>=0:
                n=n-turn
                turn-=1                
                place+=1
                if place%2==0:
                    flag=False
                elif place%2!=0:
                    flag=True
            else:
                break
            
        if flag==1:
            return True
        else:
            return False



            


        