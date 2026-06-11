'''
for every value we encounter we add to the list and sort them and return the kth 1 index number.
can run a dfs to get every element

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.l=[]
        def dfs(root):
            if not root:
                return
            self.l.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        self.l.sort()

        return self.l[k-1]
        