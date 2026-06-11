'''
for every value we encounter we add to the list and sort them and return the kth 1 index number.
can run a dfs to get every element

we can use a inorder travel on the bst to search the tree from the smallest to greatest and we can skip list.sort()
we can save an extra O(N) run time. so we can just return the k-1 index for 0th index

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
            dfs(root.left)
            self.l.append(root.val)
            dfs(root.right)
        dfs(root)
        return self.l[k-1]
        