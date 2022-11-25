# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minVal = -2**31 - 1
        maxVal = 2**31
        return self.validate(root, minVal, maxVal)

    def validate(self, node, minVal, maxVal):
        if node == None:
            return True
        elif node.val <= minVal or node.val >= maxVal:
            return False
        # Nodes on left should be between minVal and nodeVal 
        # Nodes on right should be between nodeVal and maxVal
        # As by nature of a BST the further down you go the range the numbers can be decrease by these bounds
        else:
            return self.validate(node.left, minVal, node.val) and self.validate(node.right, node.val, maxVal)