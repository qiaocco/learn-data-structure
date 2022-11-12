# 时间复杂度： O(m+n), 我们只需要遍历两个字符一次即可。
# 空间复杂度: O(S), s为全部的小写字母，s=26

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        counter1 = collections.Counter(ransomNote)
        counter2 = collections.Counter(magazine)
        if len(counter1) > len(counter2):
            return False

        for k, v in counter1.items():
            if counter2.get(k, 0) < v:
                return False

        return True