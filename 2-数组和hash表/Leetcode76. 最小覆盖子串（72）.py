class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isContain(window_dict, t_dict):
            # 当前滑动窗口是否包含t
            for key in t_dict:
                if window_dict[key] < t_dict[key]: return False
            return True
        window_dict = defaultdict(int)  # 存放当前窗口所有元素
        t_dict = defaultdict(int)       # 存放t中的所有元素 key:val
        for key in t: t_dict[key] += 1
        start = 0
        min_len = len(s) + 1
        res = ""
        for end in range(len(s)):
            if s[end] in t_dict: window_dict[s[end]] += 1
            while isContain(window_dict, t_dict):
                if min_len > (end - start + 1):
                    min_len = end - start + 1
                    res = s[start: end+1]
                window_dict[s[start]] -= 1
                start += 1
        return res