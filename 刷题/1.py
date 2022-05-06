from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = dict()
        for idx, num in enumerate(nums):
            if target - num in hashset:
                return [idx, hashset[target - num]]

            hashset[num] = idx
        return []
