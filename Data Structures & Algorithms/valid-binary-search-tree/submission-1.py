# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # in order traversal
    # root, go to left, min = -inf max = root val
    # root, go to right, min = root val, max = inf
    # return True or False depending on valid
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(curr = root, minim = -float("inf"), maxim = float("inf")):
            if not curr:
                return True

            val = curr.val
            if not(minim < val < maxim):
                return False
            
            # left
            if not helper(curr.left, minim, val):
                return False

            # right
            if not helper(curr.right, val, maxim):
                return False
            
            return True
        
        return helper()
