# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Catch edge case of empty input
        if head is None:
            return None
        # Find middle node, use as root
        # Turn values of LL into a list
        nums = []
        tmpHead = head
        while tmpHead != None:
            nums.append(tmpHead.val)
            tmpHead = tmpHead.next
        # Build tree out of linked list
        # Find the midpoint of parent to end, assign as node
        # Do this recursively
        newHead = TreeNode()
        self.buildTree(newHead, 0, len(nums)-1, nums)
        return newHead

    # Recursively build out tree
    # LC is midpoint from parent val to left end
    # RC is midpoint from parent val to right end
    def buildTree(self, node, left,right, nums):
        # Breakout case, parent of this node does not have a child in this direction, return None
        if left > right:
            return None
        # If we should be a node, initialize ourselves as a node and get our val
        if node is None:
            node = TreeNode()
        # Find mid in list, assign that value to our curNode
        mid = (left+right) // 2
        node.val = nums[mid]
        # Recursively populate subtree of curNode
        node.left = self.buildTree(node.left, left, mid-1, nums)
        node.right = self.buildTree(node.right, mid+1, right, nums)
        return node