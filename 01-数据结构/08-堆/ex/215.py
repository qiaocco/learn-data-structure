import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        lst = []
        heapq.heapify(lst)

        for num in nums:
            heapq.heappush(lst, num)

        while k > 1:
            heapq.heappop(lst)
            k -= 1
        return heapq.heappop(lst)
