# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        arr = []
        def preorder(curr = root):
            nonlocal arr
            if not curr:
                arr.append('null')
            else:
                arr.append(str(curr.val))
                preorder(curr.left)
                preorder(curr.right)
        preorder()
        return "$".join(arr)
        
            

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        arr = data.split("$")
        for i, val in enumerate(arr):
            if val == 'null':
                arr[i] = None
            else:
                arr[i] = int(val)
        
        # dfs preorder, global idx
        idx = 0
        def preorder():
            nonlocal idx
            if arr[idx] == None:
                idx += 1
                return None
            else:
                node = TreeNode(arr[idx])
                idx += 1
                node.left = preorder()
                node.right = preorder()
                return node
        return preorder()



