# 视频题解： https://www.bilibili.com/video/BV18J411j7Pb?spm_id_from=333.337.search-card.all.click

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0
        n = len(s)
        for i in range(n):
            left1, right1 = self.expand(s, i, i)
            left2, right2 = self.expand(s, i, i + 1)
            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start:end + 1]

    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - 1


if __name__ == '__main__':
    s = "babad"
    print(Solution().longestPalindrome(s))
