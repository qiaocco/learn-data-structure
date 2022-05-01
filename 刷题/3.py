class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right = -1
        st = set()
        ans = 0
        n = len(s)
        for i in range(n):
            if i != 0:
                st.remove(s[i - 1])
            while right < n - 1 and s[right + 1] not in st:
                st.add(s[right + 1])
                right += 1

            ans = max(ans, right - i + 1)

        return ans


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
