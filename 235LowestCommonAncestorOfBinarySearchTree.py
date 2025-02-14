# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        '''
        Recursive DFS solution
        '''
        # def dfs(node):
        #     if p.val<=node.val<=q.val or q.val<=node.val<=p.val:
        #         return node
        #     if p.val<node.val and q.val<node.val:
        #         return dfs(node.left)
        #     if p.val>node.val and q.val>node.val:
        #         return dfs(node.right) 
        # return dfs(root)

        '''
        Iterative solution
        '''
        while root:
            if p.val<root.val and q.val<root.val:
                root = root.left
            elif p.val>root.val and q.val>root.val:
                root = root.right
            else:
                return root

