class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u,d,l,r=0,0,0,0
        for i in moves:
            if i=="U":
                u+=1
            elif i=="D":
                d+=1
            elif i=="L":
                l+=1
            elif i=='R':
                r+=1
        if (u==d) and (l==r):
            return True
        else:
            return False
        