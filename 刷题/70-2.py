# 扩展
# 不能爬到7及7的倍数——2021.3 字节跳动-教育-后端-一面

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n + 1):
            if i % 7 == 0:
                dp[i] = 0
            else:
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


if __name__ == '__main__':
    print(Solution().climbStairs(8))
