class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        res = ""
        while i >= 0 or j >= 0:
            data1 = int(num1[i]) if i >= 0 else 0
            data2 = int(num2[j]) if j >= 0 else 0
            tmp = data1 + data2 + carry
            carry = tmp // 10
            res = str(tmp % 10) + res
            i -= 1
            j -= 1

        if carry:
            return "1" + res
        return res
