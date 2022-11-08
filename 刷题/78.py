from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtracking(start_idx, tmp):
            result.append(tmp[:])

            for i in range(start_idx, len(nums)):
                tmp.append(nums[i])
                backtracking(start_idx + 1, tmp)
                tmp.pop()

        backtracking(0, [])
        return result


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
