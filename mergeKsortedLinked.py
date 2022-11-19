# https://leetcode.com/problems/merge-k-sorted-lists/solutions/10528/a-java-solution-based-on-priority-queue/
# LEARN PRIORITY QUEUES

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        lLen = len(lists)
        if lLen == 0:
            return
        hasLen = 0
        # track number of completed lists
        numComplete = 0
        # catch non-empty input of only empty inputs
        for i in range(lLen):
            if lists[i] is None:
                numComplete += 1
            else:
                hasLen = 1
        if hasLen == 0:
            return
        result = ListNode()
        ptr = ListNode()
        ptr = result
        while numComplete < lLen:
            # Check val of each curNode in list
            minVal = 10**4 + 1
            minListIndex = -1
            # Find current minVal
            for i in range(lLen):
                if not (lists[i] is None):
                    if lists[i].val < minVal:
                        minVal = lists[i].val
                        minListIndex = i
            # update ptr
            ptr.val = minVal
            # update list
            lists[minListIndex] = lists[minListIndex].next
            # check to see if its finished
            if lists[minListIndex] == None:
                numComplete += 1
            # See if there's nodes to create
            if numComplete < lLen:
                nxt = ListNode()
                ptr.next = nxt
                ptr = ptr.next
        return result