class MyHashMap:

    def __init__(self):
        self.mapp = defaultdict(int)

    def put(self, key: int, value: int) -> None:
        self.mapp[key] = value

    def get(self, key: int) -> int:
        if key in self.mapp: return self.mapp[key]
        else: return -1

    def remove(self, key: int) -> None:
        if key in self.mapp: del self.mapp[key]