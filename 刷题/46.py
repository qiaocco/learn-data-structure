from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        size = len(nums)
        if size == 0:
            return nums

        used = [False for _ in range(size)]
        res = []
        self.dfs(nums, size, 0, [], used, res)
        return res

    def dfs(self, nums, size, depth, path, used, res):
        if depth == size:
            res.append(path[:])
            return

        for i in range(size):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])
            self.dfs(nums, size, depth + 1, path, used, res)
            used[i] = False
            path.pop()


if __name__ == '__main__':
    print(Solution().permute([1, 2, 3]))
