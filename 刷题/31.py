from typing import List


# https://leetcode.cn/problems/next-permutation/solution/xia-yi-ge-pai-lie-suan-fa-xiang-jie-si-lu-tui-dao-/
# 冒泡排序
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        i = len(nums) - 2
        j = len(nums) - 1
        k = len(nums) - 1

        # 注意边界条件511
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        # 找到大数与小数字交换
        if i >= 0:
            while nums[i] <= nums[k]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]
        # 翻转
        self.reverse(nums, j, len(nums) - 1)

        return nums

    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1


if __name__ == '__main__':
    nums = [5, 1, 1]
    print(Solution().nextPermutation(nums))
