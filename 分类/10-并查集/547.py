from typing import List


# 这个做的有问题
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = UnionFind(isConnected)
        n = len(isConnected)
        for i in range(n):
            for j in range(i + 1, len(n)):
                if isConnected[i][j] == 1:
                    uf.union(i, j)

        return uf.get_count()


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
