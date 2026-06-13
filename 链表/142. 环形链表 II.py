# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next

            if slow==fast: # 相遇
                point1=head
                point2=slow
                while point1!=point2:
                    point1=point1.next
                    point2=point2.next

                # 此时point1 和 point2 相遇在 入口
                return point1

        # 此时说明没有 环
        return None






