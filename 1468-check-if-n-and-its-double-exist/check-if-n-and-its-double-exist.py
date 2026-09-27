class Solution:
    def checkIfExist(self, arr: list[int]) -> bool:
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i]==2*arr[j]:
                    print("True cause 1st")
                    print(f"i is {arr[i]} and j is {arr[j]}")
                    return True
                elif arr[j]==2*arr[i]:
                    print("True cause 2nd")
                    print(f"i is {arr[i]} and j is {arr[j]}")
                    return True
        return False
        