from typing import List


# dfs深度优先
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        result = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    result += 1
                    self.dfs(grid, i, j, row, col)

        return result

    def dfs(self, grid, i, j, row, col):
        if i < 0 or j < 0 or i >= row or j >= col or grid[i][j] == '0':
            return

        grid[i][j] = '0'
        self.dfs(grid, i, j + 1, row, col)
        self.dfs(grid, i, j - 1, row, col)
        self.dfs(grid, i + 1, j, row, col)
        self.dfs(grid, i - 1, j, row, col)


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]

    print(Solution().numIslands(grid))
