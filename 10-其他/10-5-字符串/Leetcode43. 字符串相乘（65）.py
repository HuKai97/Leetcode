class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        num1, num2 = num1[::-1], num2[::-1]
        res = [0 for _ in range(len(num1)+len(num2)+1)]
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] += int(num1[i]) * int(num2[j])
        # print(res)    # [18, 27, 28, 13, 4, 0, 0]
        for i in range(len(res)-1):
            res[i+1] += res[i] // 10
            res[i] %= 10
        # print(res) # [8, 8, 0, 6, 5, 0, 0]
        while res and res[-1] == 0:
            res.pop()
        return ''.join(map(str, res[::-1]))