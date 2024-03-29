# Time complexity is O(N) and space complexity is O(N)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        
        def dfs(root, parent, depth):
            if not root or len(result)==2:
                return
            else:
                if root.val == x or root.val==y:
                    results.append([parent, depth])

                dfs(root.left, root, depth+1)
                dfs(root.right, root, depth+1)     
        result = []
        dfs(root, None, 0)
        
        return result[0][0]!=result[1][0] and result[0][1]==result[1][1]