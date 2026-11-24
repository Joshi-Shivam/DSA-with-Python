class Solution:
    def isThree(self, n: int) -> bool:
        count=0
        for i in range(1,n+1):
            print("Current count is ",count)
            if count>3:
                print("More than 3")
                return False
            else:
                if n%i==0:
                    print(f"{n} is divisible by {i} so count increase")
                    count+=1
        print("Current count is ",count)
        if count==3:
            return True
        else:
            return False
        