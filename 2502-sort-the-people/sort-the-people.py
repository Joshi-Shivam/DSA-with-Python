class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash={}
        for i in range(len(names)):
            if heights[i] not in hash:
                hash[heights[i]]=names[i]

        for i in range(len(heights)):
            small=i
            for j in range(i,len(heights)):
                if heights[j]>heights[small]:
                    small=j
            heights[i],heights[small]=heights[small],heights[i]
        new=[]
        for i in heights:
            if i in hash.keys():
                new.append(hash[i])
        return new

        