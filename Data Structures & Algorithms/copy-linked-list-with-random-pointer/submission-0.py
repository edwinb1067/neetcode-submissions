"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Do a hashmap pass
        my_map = {}
        curr = head
        while curr is not None:
            # Key is the node, value is the same node, but with only a value
            my_map[curr] = Node(curr.val)
            curr = curr.next
        # Second pass for linking all the nodes
        curr = head
        while curr:
            if curr.next:
                my_map[curr].next = my_map[curr.next]
            if curr.random:
                my_map[curr].random = my_map[curr.random]
            curr = curr.next

        return my_map[head] if head else None

            