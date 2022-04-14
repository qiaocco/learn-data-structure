from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        count0 = 0
        count1 = 0
        for item in position:
            if item % 2 == 0:
                count0 += 1
            else:
                count1 += 1
        return min(count0, count1)


if __name__ == '__main__':
    print(Solution().minCostToMoveChips([1, 2, 2, 2, 2]))
