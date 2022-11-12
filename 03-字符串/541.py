# 时间复杂度: O(n)
# 空间复杂度： O(n)
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        lst = list(s)

        for i in range(0, len(lst), 2 * k):
            lst[i:i+k] = reversed(lst[i:i+k])
        return ''.join(lst)

print(Solution().reverseStr("abcdefg", 2))