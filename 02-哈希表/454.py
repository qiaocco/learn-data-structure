# 时间复杂度： O(n2)
# 空间复杂度: O(n2)
# 即为哈希映射需要使用的空间。在最坏的情况下，data1+data2 的值均不相同，因此值的个数为n2, 也就需要n2的空间
# https://leetcode.cn/problems/4sum-ii/solutions/499745/si-shu-xiang-jia-ii-by-leetcode-solution/
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result = 0

        hashset = collections.Counter(data1+data2 for data1 in nums1 for data2 in nums2)
        for data3 in nums3:
            for data4 in nums4:
                # data1+data2的和
                if 0-data3-data4 in hashset:
                    result += hashset[-data3-data4]

        return result