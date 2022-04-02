from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if len(grid) == 0:
            return 0
        result = 0
        q = []
        row = len(grid)
        col = len(grid[0])

        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    result += 1
                    q.append([i, j])
                    grid[i][j] = '0'
                    while len(q) > 0:
                        cur = q.pop()
                        x = cur[0]
                        y = cur[1]
                        if grid[x][y] == "1":
                            grid[x][y] = '0'
                            result += 1

                        if x - 1 >= 0 and grid[x - 1][y] == '1':
                            q.append([x - 1, y])
                            grid[x - 1][y] = '0'
                        if y - 1 >= 0 and grid[x][y - 1] == '1':
                            q.append([x, y - 1])
                            grid[x][y - 1] = '0'
                        if x + 1 < row and grid[x + 1][y] == '1':
                            q.append([x + 1, y])
                            grid[x + 1][y] = '0'
                        if y + 1 < col and grid[x][y + 1] == '1':
                            q.append([x, y + 1])
                            grid[x][y + 1] = '0'
        return result


if __name__ == '__main__':
    grid = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]]

    print(Solution().numIslands(grid))
