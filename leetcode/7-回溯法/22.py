from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.backtracing(n, result, 0, 0, "")
        return result

    def backtracing(self, n, result, left, right, s):
        if right > left:
            return
        if left == right == n:
            result.append(s)
            return

        if left < n:
            self.backtracing(n, result, left + 1, right, s + "(")
        if right < left:
            self.backtracing(n, result, left, right + 1, s + ")")


if __name__ == '__main__':
    print(Solution().generateParenthesis(3))
