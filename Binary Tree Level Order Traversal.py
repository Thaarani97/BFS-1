#TC -O(n)
#SC -O(n)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        r = []
        q = deque()
        q.append(root)
        while q and root:
            size = len(q)
            temp = []
            while size:
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                size-=1
                
            r.append(temp)
            
        return r