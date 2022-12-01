# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Better approach, we can utilize the python id function to look at the memory location of each node. Each node we encounter, we pass into a dict, then if value in dict, we return that node
        # Not sure how python does memory storage, is it possible to do by just looking at value of address?
        addresses = {}
        tmpHead = head
        # Loop through linked list, at each node check if address is in dict already, if not add address to linked list
        while tmpHead is not None:
            # If address in dict, return node
            if addresses.get(id(tmpHead), -1) != -1:
                return tmpHead
            else:
                addresses.update({id(tmpHead) : 1})
            tmpHead = tmpHead.next
        # If we get down to here, that means no loops were encountered, return -1
        return None