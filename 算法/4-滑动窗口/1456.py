# 给你字符串 s 和整数 k 。
#
# 请返回字符串 s 中长度为 k 的单个子字符串中可能包含的最大元音字母数。
#
# 英文中的 元音字母 为（a, e, i, o, u）。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0

        i = 0
        j = k

        res = 0

        yuanyin_set = set("aeiou")

        while j < len(s) - 1:
            count = 0
            for item in s[i:j]:
                if item in yuanyin_set:
                    count += 1
            res = max(res, count)

        return res
