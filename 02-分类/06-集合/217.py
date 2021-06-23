from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        is_equal = len(nums) == len(set(nums))
        return not is_equal


