class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1: return strs[0]
        for i in range(len(strs[0])):  # 比较第i个字符
            for j in range(1, len(strs)):  # 比较第j个字符串
                # 如果第j个字符串长度就等于i个字符 或 第j个字符串的第i个字符不等于第0个字符串的第i个字符
                if i == len(strs[j]) or strs[0][i] != strs[j][i]: return strs[0][:i]
        return strs[0]