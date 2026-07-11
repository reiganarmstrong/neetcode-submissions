# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def pruneSmallest(curr):
            if not curr.left:
                return (curr.right, curr.val)
            
            curr.left, val = pruneSmallest(curr.left)

            return (curr, val)
        
        def delete(curr=root):
            if not curr:
                return
            
            if curr.val == key:
                # if both subtrees exist
                if curr.left and curr.right:
                    # prune smallest in right
                    curr.right, curr.val = pruneSmallest(curr.right)
                elif curr.left:
                    curr = curr.left
                elif curr.right:
                    curr = curr.right
                else:
                    curr = None
                return curr
            elif curr.val < key:
                curr.right = delete(curr.right)
            else:
                curr.left = delete(curr.left)
            
            return curr

        return delete()

