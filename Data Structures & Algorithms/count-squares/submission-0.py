from collections import defaultdict
class CountSquares:
    # no parallel squares
    # hashmap would be helpful
        # x: {y: count}
    # for each point in same row, try to construct a square
    def __init__(self):
        self.points = defaultdict(dict)
        

    def add(self, point: List[int]) -> None:
        self.points[point[0]]
        if point[1] not in self.points[point[0]]:
            self.points[point[0]][point[1]] = 1
        else:
            self.points[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        numSquares = 0

        if point[0] not in self.points:
            return 0
        for y in self.points[point[0]]:
            diff = abs(point[1] - y)
            if diff == 0:
                continue
            # check if -diff exists
            x = point[0] - diff
            if x in self.points and y in self.points[x] and point[1] in self.points[x]:
                numSquares += self.points[x][y] * self.points[x][point[1]] * self.points[point[0]][y]
            
            x = point[0] + diff
            if x in self.points and y in self.points[x] and point[1] in self.points[x]:
                numSquares += self.points[x][y] * self.points[x][point[1]] * self.points[point[0]][y]

        return numSquares