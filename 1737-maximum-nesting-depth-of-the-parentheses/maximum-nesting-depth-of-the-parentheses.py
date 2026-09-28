class Solution:
    def maxDepth(self, s: str) -> int:
        hash={"(":0,")":0}
        stack=[]        
        deep=0
        for i in s:
            if i in hash:
                if i=="(":
                    deep+=1
                elif i ==")":
                    stack.append(deep)
                    deep-=1
        if len(stack)==0:
            return 0
        else:
            return max(stack)
                


                

        