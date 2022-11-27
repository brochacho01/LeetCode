# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # Make two sublists, one less than x and one greater than or same as x
        # Iterate through the original list, building up these two lists, then connect the two at the end. O(n) solution
        if head is None:
            return head
        gHead = ListNode(-101)
        lHead = ListNode(-101)
        # collect head val
        ptr = head
        if ptr.val >= x:
            gHead.val = ptr.val
        else:
            lHead = ptr
        lptr = lHead
        gptr = gHead
        ptr = ptr.next
        i = 1
        # Iterate over linked list
        while ptr is not None:
            print(i)
            # If curNode val is less than x
            if ptr.val < x:
                # If lList has not been established
                if lHead.val == -101:
                    lHead.val = ptr.val
                    lptr = lHead
                # else make a new node for lptr, move to new node, and assign it that value
                else:
                    lptr.next = ListNode()
                    lptr = lptr.next
                    lptr.val = ptr.val
            # Else val is greater than x, same logic
            else:
                if gHead.val == -101:
                    gHead.val = ptr.val
                    gptr = gHead
                else:
                    gptr.next = ListNode()
                    gptr = gptr.next
                    gptr.val = ptr.val
            ptr = ptr.next
            i += 1
        # Here all nodes of list should either ge in lList or gList
        gptr.next = None
        # if lHead does not exist, just return gHead
        if lHead.val == -101:
            return gHead
         # if gHead exists and lHead exists attach the two
        elif gHead.val != -101 and lHead.val != -101:
            lptr.next = gHead
        # if we get here, then gList has not been established
        elif gHead.val == -101:
            lptr.next = None
            return lHead
        return lHead