class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n==10:
            return True
        place=0
        turn=10
        bob=0
        alice=0
        while n>0:
            if (n-turn)>=0:
                n=n-turn
                turn-=1                
                place+=1
                print(f"{place} chance ")
                if place%2==0:
                    print(f"Bob wins round current n is {n}")
                    bob=1
                    alice=0
                elif place%2!=0:
                    print(f"Alice wins round current n is {n}")
                    alice=1
                    bob=0
            else:
                break
            
        if alice==1:
            return True
        else:
            return False



            


        