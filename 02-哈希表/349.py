# 时间复杂度：O(m+n), m,n为数组长度
# 使用两个集合分别存储两个数组中的元素需要 O(m+n)的时间，遍历较小的集合并判断元素是否在另一个集合中需要 O(min⁡(m,n)) 的时间，因此总时间复杂度是 O(m+n)。
# 空间复杂度: O(m+n)，其中 m 和 n 分别是两个数组的长度。空间复杂度主要取决于两个集合。

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        s1 = set(nums1)
        s2 = set(nums2)
        for item in s1:
            if item in s2:
                result.append(item)

        return result

    def set_intersection(s1, s2: set):
        result = []
        if len(s1) < len(s2):
            return self.set_intersection(s2, s1)
        for item in s1:
            if item in s2
                result.append(item)

        return result