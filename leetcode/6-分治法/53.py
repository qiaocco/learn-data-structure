from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.do_get_max(nums, 0, len(nums) - 1)

    def do_get_max(self, nums, left, right):
        if left == right:
            return nums[left]

        mid = left + (right - left) // 2
        left_sum = self.do_get_max(nums, left, mid)
        right_sum = self.do_get_max(nums, mid + 1, right)
        cross_sum = self.cross_sum(nums, left, right)

        return max(left_sum, right_sum, cross_sum)

    def cross_sum(self, nums, left, right):
        mid = left + (right - left) // 2
        left_sum = nums[mid]
        left_max = left_sum
        for i in range(mid - 1, left-1, -1):
            left_sum += nums[i]
            left_max = max(left_max, left_sum)

        right_sum = nums[mid + 1]
        right_max = right_sum
        for i in range(mid + 2, right + 1, 1):
            right_sum += nums[i]
            right_max = max(right_max, right_sum)

        return left_max + right_max


if __name__ == '__main__':
    nums = [5, 4, -1, 7, 8]
    print(Solution().maxSubArray(nums))
