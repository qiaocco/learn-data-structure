class Solution:
    def climbStairs(self, n: int) -> int:
        p = 0
        q = 1
        for i in range(1, n):
            temp = p + q
            p = q
            q = temp

        return p + q


if __name__ == '__main__':
    print(Solution().climbStairs(8))
