class Solution:
    def romanToInt(self, s: str) -> int:
        rom={
            "i":1,
            "v":5,
            "x":10,
            "l":50,
            "c":100,
            "d":500,
            "m":1000
        }
        
        s=s.lower()
        num=0
        temp=0
        i=0
        while i<len(s):
            if i>len(s)-1:
                break
            else:
                if i+1<len(s) and rom[s[i]]<rom[s[i+1]]:
                    temp=rom[s[i+1]]-rom[s[i]]
                    num+=temp
                    i+=2
                else:
                    num+=rom[s[i]]
                    print()
                    i+=1
                    
        return num