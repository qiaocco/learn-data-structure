from typing import List
import copy


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            temp = []
            for item in result:
                r = copy.deepcopy(item)
                r.append(num)
                temp.append(r)
            for t in temp:
                result.append(t)

        return result


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
