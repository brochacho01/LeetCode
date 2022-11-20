# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lLen = len(lists)
        # Catch empty input
        if lLen == 0:
            return
        # Catch non-empty input of all empty lists
        hasEmpty = 1
        for i in range(lLen):
            if lists[i] is not None:
                hasEmpty = 0
                break
        if hasEmpty == 1:
            return
        # Take priority queue approach. Place all elements into list then turn it into a priority queue using the pqueue library
        pQueue = []
        for i in range(lLen):
            while lists[i] is not None:
                pQueue.append(lists[i].val)
                lists[i] = lists[i].next
        heapq.heapify(pQueue)
        # Now place all elements from the priority queue into linked list and return
        head = ListNode()
        head.val = heapq.heappop(pQueue)
        ptr = ListNode
        ptr = head
        while len(pQueue) > 0:
            nxt = ListNode()
            nxt.val = heapq.heappop(pQueue)
            ptr.next = nxt
            ptr = ptr.next
        return head