class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4: return []
        def isMeeting(patch):
            # 长度不能小于1或者大于3
            if len(patch) < 1 or len(patch) > 3: return False
            # 长度大于1时不能以0开头
            if len(patch) > 1 and patch[0] == '0': return False
            # 长度等于3时不能大于255
            if len(patch) == 3:
                count = int(patch[0])*100 + int(patch[1])*10 + int(patch[2])
                if count > 255: return False
            return True
        def backtracking(start, path, res, s, depth):
            if depth == 3:
                if isMeeting(s[start:]):
                    res.append('.'.join(path + [s[start:]]))
                    return
            for i in range(start, len(s)):
                if isMeeting(s[start:i+1]):
                    path.append(s[start:i+1])
                    backtracking(i+1, path, res, s, depth+1)
                    path.pop()
        res, path = [], []
        backtracking(0, path, res, s, 0)
        return res