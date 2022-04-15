class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        d = dict()
        d[0] = 0
        d[1] = 1

        for i in range(2, n + 1):
            d[i] = d[i - 1] + d[i - 2]

        return d[n]


if __name__ == '__main__':
    print(Solution().fib(25))
