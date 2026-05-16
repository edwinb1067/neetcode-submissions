# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Add each value for each spot, go through the loop again making sure that there are no digits greater than 10
        sum_next = 0
        currl1 = l1
        currl2 = l2
        dummy = ListNode(0, None)
        prev = dummy
        while currl1 or currl2:
            val1 = currl1.val if currl1 else 0
            val2 = currl2.val if currl2 else 0
            curr_val =  val1 + val2 + sum_next
            if curr_val > 9:
                sum_next = curr_val // 10
            else:
                sum_next = 0
            node = ListNode(curr_val % 10, None)
            prev.next = node
            prev = node
            currl1 = currl1.next if currl1 else None
            currl2 = currl2.next if currl2 else None

        if sum_next != 0:
            prev.next = ListNode(sum_next, None)

        return dummy.next