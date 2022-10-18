class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 先按身高h进行降序排序  再按k进行插入
        # 局部最优：优先按身高高的people的k来插入。插入操作过后的当前元素满足队列属性
        # 全局最优：最后都做完插入操作，整个队列满足题目队列属性
        people.sort(key = lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)   # idx 元素
        return queue