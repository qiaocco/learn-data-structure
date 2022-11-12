# https://leetcode.cn/problems/3sum/solutions/39722/pai-xu-shuang-zhi-zhen-zhu-xing-jie-shi-python3-by/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        nums.sort()
        for i in range(n):
            left = i+1
            right = n-1

            if nums[i] > 0:
                return result

            if i> 0 and nums[i] == nums[i-1]:
                continue

            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    while left < right and nums[left] == nums[left+1]:
                        left += 1

                    right -= 1
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left += 1

        return result