from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        row = len(grid)
        col = len(grid[0])
        waters = 0
        uf = UnionFind(grid)
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '0':
                    waters += 1
                else:
                    directions = [(0, 1), (1, 0), (-1, 0), (1, 0)]
                    for x, y in directions:
                        x = x + i
                        y = y + j
                        if 0 <= x < row and 0 <= y < col and grid[x][y] == "1":
                            uf.union(x * col + y, i * col + j)

        return uf.get_count() - waters


class UnionFind:
    def __init__(self, grid):
        row = len(grid)
        col = len(grid[0])
        self.root = [-1] * (row * col)
        self.count = row * col
        for i in range(row * col):
            self.root[i] = i

    def find(self, x):
        if x == self.root[x]:
            return x
        return self.find(self.root[x])

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            self.root[rootx] = rooty
            self.count -= 1

    def get_count(self):
        return self.count
