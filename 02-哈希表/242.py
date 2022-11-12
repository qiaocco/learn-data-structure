# 时间复杂度： O(n), n为s的长度
# 空间复杂度: O(s)， s为字符集的大小， 此处s=26

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for item in s:
            record[ord(item) - ord('a')] +=1

        for item in t:
            record[ord(item) - ord('a')] -= 1

        for item in record:
            if item != 0:
                return False

        return True