class Solution:
    def isHappy(self, n: int) -> bool:
        def get_total(num):
            total = 0
            while num > 0:
                num, mod = divmod(num, 10)
                total += mod ** 2
            return total

        seen = set()

        while True:
            n = get_total(n)
            if n == 1:
                return True
            if n not in seen:
                seen.add(n)
            else:
                return False
