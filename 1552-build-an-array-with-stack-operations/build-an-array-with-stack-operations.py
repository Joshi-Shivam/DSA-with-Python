class Solution:
    def buildArray(self, target: list[int], n: int) -> list[str]:
        stack=[]
        temp=[]
        count=1
        hash={}
        for i in target:
            hash[i]=0
        while temp!=target:            
            if count in hash:
                stack.append("Push")
                temp.append(count)
                count+=1
            else:
                stack.append("Push")
                stack.append("Pop")
                count+=1
        return stack


        