class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        i,j=0,1
        print(arr)
        res=[]
        min=arr[j]-arr[i]
        while j<len(arr):
            print(f"Current min {min}")
            temp=[]
            if arr[j]-arr[i]==min:
                min=arr[j]-arr[i]
                temp.append(arr[i])
                temp.append(arr[j])
                print(f"Current temp {temp}")
                res.append(temp)
                temp=[]
            elif arr[j]-arr[i]<min:
                res=[]
                min=arr[j]-arr[i]
                temp.append(arr[i])
                temp.append(arr[j])
                print(f"Current temp {temp}")
                res.append(temp)
                temp=[]
            i+=1
            j+=1
        return res

                

        
         


        