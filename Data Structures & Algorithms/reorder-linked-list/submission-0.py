# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle
        slow, fast = head, head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        # Reverse second half of the list
        new_list = slow.next
        slow.next = None
        prev = None
        while new_list:
            temp = new_list.next
            new_list.next = prev
            prev = new_list
            new_list = temp
        # Iterate through both loops
        first = head
        new_list = prev
        while new_list:
            tmp1 = first.next
            tmp2 = new_list.next
            first.next = new_list
            new_list.next = tmp1
            first = tmp1
            new_list = tmp2