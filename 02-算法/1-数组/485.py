from typing import List


# 时间复杂度 O(n)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = max_count = 0
        for item in nums:
            if item == 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 0

        max_count = max(max_count, count)
        return max_count


if __name__ == '__main__':
    print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
