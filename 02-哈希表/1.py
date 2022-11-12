# 时间复杂度: O(n)
# 空间复杂度： O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = dict()

        for i, data in enumerate(nums):
            if target-data in hashset:
                return [i, hashset[target-data]]

            hashset[data] = i

