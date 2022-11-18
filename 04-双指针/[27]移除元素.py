#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            if nums[left] == val:
                print(f'left={left}, right={right}, nums={nums}')
                nums[left] = nums[right]
                print(f'left={left}, right={right}, nums={nums}')
                right -= 1
            else:
                left += 1
        return left


# @lc code=end
