from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = dict()
        for item in nums:
            if item not in d:
                d[item] = 1
            else:
                d[item] += 1

        for k, v in d.items():
            if v > len(nums) / 2:
                return k
