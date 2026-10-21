class Solution:
    def findCenter(self, edges: list[list[int]]) -> int:
        hash={}
        for i in edges:
            for j in i:
                if j in hash:
                    hash[j]+=1
                else:
                    hash[j]=1
        print(hash)
        for i in hash:
            if hash[i]==len(edges):
                return i
        