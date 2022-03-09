from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        i = 0
        j = 0
        total = 0
        res = len(nums) + 1

        while j <= len(nums) - 1:
            total = total + nums[j]
            j += 1
            while total >= target:
                res = min(res, j - i)
                total -= nums[i]
                i += 1

        if res == len(nums) + 1:
            return 0
        return res


if __name__ == '__main__':
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    print(Solution().minSubArrayLen(target, nums))
