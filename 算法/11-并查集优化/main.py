class UnionFind:
    def __init__(self, grid):
        row = len(grid)
        col = len(grid[0])
        self.root = [-1] * (row * col)
        self.rank = [0] * (row * col)
        self.count = row * col
        for i in range(row * col):
            self.root[i] = i

    def find(self, x):
        if x == self.root[x]:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.root[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.root[rootx] = rooty
            else:
                self.root[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1

    def get_count(self):
        return self.count
