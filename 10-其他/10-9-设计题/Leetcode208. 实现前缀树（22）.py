class TreeNode:
    def __init__(self):
        self.children = defaultdict(TreeNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            cur = cur.children[c]
        cur.is_word = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            # dict.get(key, default=None)
            cur = cur.children.get(c, None)
            if cur is None: return False
        return cur.is_word

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            cur = cur.children.get(c, None)
            if cur == None: return False
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)