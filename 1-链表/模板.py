"""
@Author: HuKai
@Date: 2022/6/1  10:09
@github: https://github.com/HuKai97
"""
# 找到链表中点
'''
# 情况一
slow, fast = head, head.next
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
奇数找到中点 如：4 2 1 3 5    slow=1
偶数找到中点前面一个 4 2 1 3   slow=2

# 情况二
slow, fast = head, head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
奇数找到中点 如：4 2 1 3 5    slow=1
偶数找到中点后面一个 4 2 1 3   slow=1
'''