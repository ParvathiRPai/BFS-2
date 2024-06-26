# Time complexity is O(N) and space complexity is O(N)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """       
        if not root:
            return []
        q=collections.deque([root])
        result = []
        
        while q:
            result .append(q[-1].val)
            newQ=[]            
            for elem in q:
                if elem.left:
                    newQ.append(elem.left)
                if elem.right:
                    newQ.append(elem.right)
            q = newQ 
        return result  