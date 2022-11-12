from typing import List
import copy


# 回溯法
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for length in range(1, len(nums) + 1):
            self.backtracking(nums, result, length, 0, [])
        return result

    def backtracking(self, nums, result, length, index, subset):
        """
        :param nums:
        :param result:
        :param length: 子集的长度
        :param index:  从哪个索引开始找
        :param subset: 子集
        :return:
        """
        if len(subset) == length:
            result.append(subset[:])
            return

        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.backtracking(nums, result, length, i + 1, subset)
            subset.pop()


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
