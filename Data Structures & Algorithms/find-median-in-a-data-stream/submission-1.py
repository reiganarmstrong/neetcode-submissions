from heapq import heapify, heappush, heappop


# we want to have two list like data structures
# to easily keep track of middle two values
# likely two heaps
# one min heap and one max heap
# keep the sizes of the two heaps the same or differ by only one
# when we add we want to see the largest of the smaller side and smallest of the larger side
# max heap of first half
# min heap of second half
# after adding, if the sizes differ more than one, reorganize O(logn)
class MedianFinder:
    def __init__(self):
        # max heap
        self.first = []
        # min heap
        self.second = []

    def addFirst(self, num):
        heappush(self.first, -num)

    def addSecond(self, num):
        heappush(self.second, num)

    def addNum(self, num: int) -> None:
        if len(self.first) == 0:
            self.addFirst(num)
            return

        if num > -self.first[0]:
            self.addSecond(num)
        else:
            self.addFirst(num)

        diff = len(self.first) - len(self.second)
        if diff == -2:
            self.addFirst(heappop(self.second))
        elif diff == 2:
            self.addSecond(-heappop(self.first))

        print(self.first)
        print(self.second)

    def findMedian(self) -> float:
        totalLen = len(self.first) + len(self.second)
        if totalLen % 2 == 0:
            return (-self.first[0] + self.second[0]) / 2

        if len(self.first) > len(self.second):
            return -self.first[0]
        else:
            return self.second[0]
