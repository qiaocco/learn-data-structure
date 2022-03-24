from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.get_majority(nums, 0, len(nums) - 1)

    def get_majority(self, nums, left, right):
        if left == right:
            return nums[left]

        mid = left + (right - left) // 2

        left_major = self.get_majority(nums, left, mid)
        right_major = self.get_majority(nums, mid + 1, right)
        if left_major == right_major:
            return left_major
        left_count = 0
        right_count = 0
        for item in nums[left:right + 1]:
            if item == left_major:
                left_count += 1
            if item == right_major:
                right_count += 1

        if left_count > right_count:
            return left_major
        else:
            return right_major


if __name__ == '__main__':
    nums = [6, 5, 5]
    print(Solution().majorityElement(nums))
