from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        if len(people) == 0:
            return 0

        people.sort()
        num = 0
        i = 0
        j = len(people) - 1
        while i <= j:
            if people[i] + people[j] > limit:
                num += 1
                j -= 1
            else:
                num += 1
                i += 1
                j -= 1
        return num


Solution().numRescueBoats([3, 2, 4, 5], 6)
