from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0  # 可以到达的最远位置
        for idx in range(len(nums)):
            if reach < idx:
                return False
            reach = max(reach, idx + nums[idx])

        return True


if __name__ == '__main__':
    print(Solution().canJump([3, 2, 1, 0, 4]))
