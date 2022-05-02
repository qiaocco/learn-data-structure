from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx = nums[0]
        for i in range(1, len(nums)):
            if nums[i] + nums[i - 1] > nums[i]:
                nums[i] += nums[i - 1]

            mx = max(mx, nums[i])

        return mx
