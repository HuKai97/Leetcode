class Solution:
    def simplifyPath(self, path: str) -> str:
        # ..   .   avc   空
        if not path: return '/'
        stack = []
        path = path.split('/')
        for i in range(len(path)):
            if path[i] == '..':
                if stack: stack.pop()
            elif path[i] == '.' or path[i] == '': continue
            else: stack.append(path[i])
        # 中间以/相连
        return '/' + '/'.join(stack)