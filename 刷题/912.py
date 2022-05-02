import random
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def partition(arr, low, high):
            pivot_idx = random.randint(low, high)
            arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]
            pivot = arr[low]

            left, right = low, high
            while left < right:
                while arr[right] >= pivot and left < right:
                    right -= 1

                arr[left] = arr[right]

                while arr[left] <= pivot and left < right:
                    left += 1
                arr[right] = arr[left]

            arr[left] = pivot

            return left

        def quicksort(arr, low, high):
            if low >= high:
                return
            mid = partition(arr, low, high)
            quicksort(arr, low, mid - 1)
            quicksort(arr, mid + 1, high)

        quicksort(nums, 0, len(nums) - 1)

        return nums


if __name__ == '__main__':
    nums = [3, 1, 2, 5, 4]
    print(Solution().sortArray(nums))
    print(nums)
