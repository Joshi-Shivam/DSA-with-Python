class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        i=0
        j=len(colors)-1
        res=0
        while i<j:
            if colors[i]!=colors[j]:
                res=j-i
                break
            else:
                j-=1
        i=0
        j=len(colors)-1
        while i<j:
            if colors[i]!=colors[j]:
                if (j-i)>res:
                    res=j-i
                break
            else:
                i+=1
        return res

        