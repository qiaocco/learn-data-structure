class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s) - 1):
            for j in range(i + 1, len(s) - 1):
                if s[i] == s[j]:
                    print(i, j)
                    num = 1
                    while i + num <= j - num:
                        if s[i + num] != s[j - num]:
                            break
                        else:
                            num += 1

                    return s[i:j + 1]


if __name__ == '__main__':
    s = "cbbd"
    print(Solution().longestPalindrome(s))
