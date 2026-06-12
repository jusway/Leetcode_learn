from multiprocessing import dummy
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        current=dummy
        while list1!=None and list2!=None:
            if list1.val<=list2.val: # 拼上去list1的值
                current.next=list1
                list1=list1.next
                current=current.next
            else: # 拼上去list2的值
                current.next=list2
                list2=list2.next
                current=current.next

        if list1==None:
            current.next=list2
        else: # list2悬空
            current.next=list1

        return dummy.next





