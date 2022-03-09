from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target:  int) -> int:
        n = len(nums)
        first = 0
        last = n - 1
        while first <= last:
            mid = (first + last) // 2
            if nums[mid] > target:
                last = mid - 1
            elif nums[mid] < target:
                first = mid + 1
            else:
                return mid

        return first


if __name__ == '__main__':
    print(Solution().searchInsert(nums=[1, 3, 5, 6], target=2))
