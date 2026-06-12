from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution1:
    # 新创建一个链表
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=None
        while head!=None:
            cur=ListNode(head.val,cur)
            head=head.next

        return cur




class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        pre=None
        while head!=None:
            # 提前记录下一个节点
            next_node=head.next
            # 当前节点的next指针进行反转
            head.next=pre
            # 移动
            pre=head
            head=next_node

        return pre















