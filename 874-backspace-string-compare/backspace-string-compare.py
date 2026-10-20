class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stacka=[]
        stackb=[]
        for i in s:
            if len(stacka)==0 and i!="#":
                stacka.append(i)
            else:
                if i=="#":
                    if len(stacka)==0:
                        continue
                    else:
                        stacka.pop()
                else:
                    stacka.append(i)
        for j in t:
            if len(stackb)==0 and j!="#":
                stackb.append(j)
            else:
                if j=="#":
                    if len(stackb)==0:
                        continue
                    else:
                        stackb.pop()
                else:
                    stackb.append(j)
        if stacka==stackb:
            return True
        else:
            return False
        