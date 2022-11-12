def partition(nums, left, right):
    pivot = nums[left]
    i, j = left, right
    while i < j:
        while i < j and nums[j] >= pivot:
            j -= 1
        nums[i] = nums[j]
        while i < j and nums[i] <= pivot:
            i += 1
        nums[j] = nums[i]

    nums[i] = pivot
    return i


def quicksort(nums, left, right):
    if left >= right:
        return

    index = partition(nums, left, right)
    quicksort(nums, left, index - 1)
    quicksort(nums, index + 1, right)


if __name__ == '__main__':
    nums = [3, 4, 1, 5, 2]
    quicksort(nums, 0, len(nums) - 1)
    print(nums)
