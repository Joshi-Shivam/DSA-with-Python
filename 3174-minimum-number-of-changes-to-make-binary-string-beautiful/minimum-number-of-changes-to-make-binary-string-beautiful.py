class Solution:
    def minChanges(self, s: str) -> int:
        i=0
        j=1
        count=0
        while j<len(s):
            if s[i]!=s[j]:
                count+=1
                i+=2
                j+=2
            else:
                i+=2
                j+=2
        return count
        