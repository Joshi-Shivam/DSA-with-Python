class Solution:
    def minOperations(self, logs: list[str]) -> int:
        stack=[]
        i=0
        while i<len(logs):
            print(stack,len(stack))
            if logs[i]=="./":
                i+=1
            else:
                if len(stack)==0:
                    if logs[i]=="../":
                        i+=1
                    else:
                        stack.append(logs[i])
                        i+=1
                else:
                    if logs[i]=="../":
                        stack.pop()
                        i+=1
                    else:
                        stack.append(logs[i])
                        i+=1
        return len(stack)


        