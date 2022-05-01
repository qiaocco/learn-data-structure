from typing import List
import heapq


# 方法1
#         nums.sort(reverse=True)
#         return nums[k - 1]
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # python中只有最小堆, 没有最大堆
        # 需要取相反数
        minheap = []
        heapq.heapify(minheap)

        for num in nums:
            heapq.heappush(minheap, -num)

        while k > 1:
            heapq.heappop(minheap)
            k -= 1

        return -minheap[0]
