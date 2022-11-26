# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # check for empty input edge case
        if head is None or head.next is None or k == 0:
            return head
        # Previous solution didn't work, instead, place all nodes into a list and do rotating
        tmpHead = head
        nodes = []
        while tmpHead is not None:
            nodes.append(tmpHead)
            tmpHead = tmpHead.next
        # k can be very large but if it's > len then it's same as % len list
        k = k % len(nodes)
        if k == 0:
            return head
        # Now we have collected all of our nodes
        # Need to rotate k times
        # Just move nodes around in list k times then reconstruct connections afterward
        for i in range(k):
            # Shift everything forward by one, node at end will get cruched, store in tmp
            tmp = nodes[-1]
            for j in range(len(nodes)-1,0,-1):
                nodes[j] = nodes[j-1]
            nodes[0] = tmp
        # Break all connections for reconstruction
        for i in range(len(nodes)):
            nodes[i].next = None
        # now reconstruct the linked list
        print(nodes)
        tmpHead = nodes[0]
        for i in range(len(nodes)-1):
            nodes[i].next = nodes[i+1]
        tmpHead = nodes[0]
        return tmpHead