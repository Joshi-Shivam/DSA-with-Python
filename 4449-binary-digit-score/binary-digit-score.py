class Solution:
    def calculateScore(self, a: int, b: int) -> int:
        aone=0
        bone=0
        while a>0:
            if a%2==1:
                aone+=1
            a=a//2
        
        while b>0:
            if b%2==1:
                bone+=1
            b=b//2
        if aone>=bone:
            return aone*bone
        else:
            return bone//aone
        