class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr=list(s.split())    
        return len(arr[-1])