class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        def heapify(tree, n, i):
            c1, c2 = 2*i+1, 2*i+2
            min_idx = i
            if c1 < n and tree[c1][1] < tree[min_idx][1]:
                min_idx = c1
            if c2 < n and tree[c2][1] < tree[min_idx][1]:
                min_idx = c2
            if min_idx != i:
                tree[i], tree[min_idx] = tree[min_idx], tree[i]
                heapify(tree, n, min_idx)
        def build_heap(tree, n):
            last_node = n - 1
            parent = (last_node - 1) // 2
            for i in range(parent, -1, -1):
                heapify(tree, n, i)
        mapp = defaultdict(int)
        for i in range(len(nums)):
            mapp[nums[i]] += 1  # defaultdict(<class 'int'>, {1: 3, 2: 2, 3: 1})
        mapp = list(mapp.items())  # [(1, 3), (2, 2), (3, 1)]
        hp = mapp[:k]
        build_heap(hp, k)
        for i in range(k, len(mapp)):
            if mapp[i][1] > hp[0][1]:
                hp[0] = mapp[i]
                heapify(hp, k, 0)
        return [x[0] for x in hp]