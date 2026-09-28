class Solution:
    def checkRecord(self, s: str) -> bool:
        hash={}
        for i in s:
            if i=='A':
                if i in hash:
                    hash[i]+=1
                else:
                    hash[i]=1
        i=0
        print(hash)
        late=""
        while i<len(s):
            print("Current idx ",s[i])
            print("Current late ",late)
            if late=="LLL":
                return False
            if s[i]=="L":
                late+="L"
            else:
                late=""
            i+=1
        if late=="LLL":
                return False
        try:
            if hash["A"]>=2:
                return False
        except KeyError:
            print("No absents")
            
        return True
            


        