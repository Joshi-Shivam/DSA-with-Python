class Solution:
    def checkString(self, s: str) -> bool:
        i=0
        j=1
        while j<len(s):
            if s[i]=="b":
                if s[j]=="a":
                    return False                
            i+=1
            j+=1
        return True