class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        double=0
        single=0
        for i in nums:
            if i<10:
                single+=i
            elif i>=10:
                double+=i
        if single==double:
            return False
        else:
            return True
        