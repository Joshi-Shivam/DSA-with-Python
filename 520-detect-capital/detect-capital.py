class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word)==1:
                return True
        if ord(word[0]) in range(97,123):
            low=1
            for i in word:
                if ord(i) not in range(97,123):
                    low=0
                    return False
            if low==1:
                return True
        elif ord(word[0]) in range(65,91):
            arr=[]
            for i in range(1,len(word)):
                arr.append(word[i])
            flag=1
            if ord(arr[0]) in range(97,123):
                for i in arr:
                    if ord(i) not in range(97,123):
                        flag=0
                        return False
            else:
                for i in arr:
                    if ord(i) not in range(65,91):
                        flag=0
                        return False
            if flag==1:
                return True




        