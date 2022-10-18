"""
@Author: HuKai
@Date: 2022/5/31  22:24
@github: https://github.com/HuKai97
"""
# https://www.bilibili.com/video/BV12z4y1o7jy?spm_id_from=333.337.search-card.all.click
class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cur_size = 0
        # 初始化hashmap key:key  val:ListNode  方便get函数直接获取O(0)
        self.ListNodeMap = dict()
        # 初始化双向链表 新建头尾节点
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.next = self.head

    def moveToHead(self, node):
        # remove from cur pos
        node.pre.next = node.next
        node.next.pre = node.pre
        # insert into self.head next
        node.next = self.head.next
        self.head.next.pre = node
        node.pre = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.ListNodeMap:
            node = self.ListNodeMap[key]
            self.moveToHead(node)
            return node.val
        else: return -1

    def addToHead(self, node):
        self.cur_size += 1
        # add node to self.head next
        node.next = self.head.next
        self.head.next.pre = node
        node.pre = self.head
        self.head.next = node
        # check capacity
        if self.cur_size > self.capacity:
            deleteNode = self.tail.pre
            deleteNode.pre.next = self.tail
            self.tail.pre = deleteNode.pre
            self.cur_size -= 1
            self.ListNodeMap.pop(deleteNode.key)

    def put(self, key: int, value: int) -> None:
        # 双向链表 -> O(0)
        if key in self.ListNodeMap:
            node = self.ListNodeMap[key]
            node.val = value
            self.moveToHead(node)
        else:
            node = ListNode(key, value)
            self.ListNodeMap[key] = node
            self.addToHead(node)