"""
@Author: HuKai
@Date: 2022/6/1  10:09
@github: https://github.com/HuKai97
"""


'''
一、找到链表中点（重要）
情况1
slow, fast = head, head.next
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
奇数找到中点 如：4 2 1 3 5    slow=1
偶数找到中点前面一个 4 2 1 3   slow=2

情况2
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
奇数找到中点 如：4 2 1 3 5    slow=1
偶数找到中点后面一个 4 2 1 3   slow=1
'''






'''
二、反转链表（重要）
def reverseList(self, head: ListNode) -> ListNode:  # 头插法  1234
    if not head or not head.next: return head
    pre = None
    cur = head
    while cur:
        temp = cur.next
        cur.next = pre
        pre = cur
        cur = temp
    return pre  # return的是尾巴  4321
    
    
for i in range(right-left+1):   # 尾插法
    temp = cur.next
    cur.next = pre.next
    pre.next = cur
    cur = temp
'''







'''
三、合并两个有序链表
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        p, q = list1, list2
        dummy = ListNode(-1)
        rear = dummy
        while p and q:
            if p.val <= q.val:
                rear.next = p
                rear = rear.next
                p = p.next
            else:
                rear.next = q
                rear = rear.next
                q = q.next
        rear.next = p if p else q
        return dummy.next
'''








'''
四、堆排序
hp = []
heapq.heappush(hp, val)   在最小堆中插入val 仍然维持这个最小堆
heapq.heappop(hp)         在最小堆中删除堆顶原始(最小值) 仍然维持这个最小堆
'''




'''
五、链表排序 归并排序
def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # 归并排序
    if not head or not head.next: return head
    # 找到链表中点  奇数找到中点   偶数找到中点前面一个数
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # 把链表切成两部分，再对这俩个部分进行排序
    head2 = slow.next
    slow.next = None
    left = self.sortList(head)
    right = self.sortList(head2)
    # 合并两个有序链表
    return self.merge(left, right)
'''