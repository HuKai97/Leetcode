class Solution:
    def reverseWords(self, s: str) -> str:
        def removeSpaces(s):
            # 去除开头结尾和中间多余空格 以及单词之间的多余的空格
            left, right = 0, len(s) - 1
            # 去除开头空格和结尾空格
            while left < right and s[left] == ' ': left += 1
            while left < right and s[right] == ' ': right -= 1
            new_s = []
            while left <= right:
                if s[left] != ' ': new_s.append(s[left])
                elif s[left] == ' ' and new_s[-1] != ' ': new_s.append(s[left])
                left += 1
            return new_s
        def reverseString(s):
            # 翻转字符串
            left, right = 0, len(s) - 1
            while left < right:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            return s
        def reverseEachWord(s):
            left, right = 0, 0
            n = len(s)
            while left < n:
                while right < n and s[right] != ' ':
                    right += 1
                # s[left: right]就是一个单词
                s[left: right] = reverseString(s[left: right])
                left = right + 1  # s[right]=' '
                right += 1
            return s
        s = removeSpaces(s)
        s = reverseString(s)
        s = reverseEachWord(s)
        return ''.join(s)


# 掉包
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = s[::-1]
        start, end = 0, 0
        # print(s)  # ['blue', 'is', 'sky', 'the']
        return ' '.join(s)