class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        for i in range(1,10000000000):
            if i%2==0 and i%n==0:
                return i
        