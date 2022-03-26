from typing import List
import copy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        self.dfs(nums, result, 0, [])
        return result

    def dfs(self, nums, result, index, subset):
        if index == len(nums):
            result.append(subset[:])
            return

        for idx in range(index, len(nums)):
            subset.append(nums[idx])
            self.dfs(nums, result, idx + 1, subset)
            subset.pop()


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
