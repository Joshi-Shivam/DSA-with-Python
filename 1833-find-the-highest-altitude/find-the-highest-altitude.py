class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        pre=[]
        count=0
        pre.append(count)
        for i in gain:
            count+=i
            pre.append(count)
        return max(pre)

        