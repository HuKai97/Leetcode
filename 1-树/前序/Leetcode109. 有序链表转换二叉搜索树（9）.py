# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head: return None
        if not head.next: return TreeNode(head.val)
        def findMid(head):
            pre = None
            slow, fast = head, head
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            return pre, slow
        pre, mid = findMid(head)
        pre.next = None
        head2 = mid.next
        root = TreeNode(mid.val)
        # print(head)
        # print(head2)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(head2)
        return root