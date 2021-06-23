from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d = dict()
        for item in nums:
            if item in d:
                return True
            d[item] = 1
        return False



