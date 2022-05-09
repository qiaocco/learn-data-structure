class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) // 2 == 0:
            return False
        pairs = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = ["?"]
        for ch in s:
            if ch in pairs:
                stack.append(ch)
            else:
                data = stack.pop()
                if pairs.get(data) != ch:
                    return False

        return len(stack) == 1


if __name__ == '__main__':
    s = "()[]{}"
    print(Solution().isValid(s))
