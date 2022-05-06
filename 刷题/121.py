from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        inf = int(1e9)
        min_price = inf
        max_profit = 0
        for price in prices:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)

        return max_profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
