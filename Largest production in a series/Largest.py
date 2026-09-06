# practicing a static sliding window technique o(n * k)

class Static:

    def __init__(self, arr : list, key=5) :
        self.arr = arr
        self.key = key

    def Solve(self) -> int :
        """At this time I'm gonna find the largest production in a array with a key = 5"""

        # We assume that the length of our array is greater than 5
        current : list = self.arr[:self.key]
        largest : list = []

    