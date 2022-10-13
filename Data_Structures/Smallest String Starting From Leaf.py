# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    vc = []
    
    def smallest(self, root, s):
        if (root == None):
            return
        
        s = chr(97+root.val)+s
        if (root.left==None and root.right==None):
            self.vc.append(s)
            return
        
        self.smallest(root.left, s)
        self.smallest(root.right, s)    

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.smallest(root,"")
        
        ans = sorted(self.vc)
        ans = ans[0]
        self.vc.clear()
        return ans

        
