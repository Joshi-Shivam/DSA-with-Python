class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        check={
            "}":"{",
            "]":"[",
            ")":"("
        }
        for i in s:
            if len(stack)==0 and i in [")","]","}"]:
                return False
            else:
                if i in {"(","[","{"}:
                    stack.append(i)
                else:
                    if stack[-1]==check[i]:
                        stack.pop()
                    else:
                        return False
        if len(stack)==0:
            return True
        else:
            return False