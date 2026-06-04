# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        maxlength=0
        if not root: #you can get rid of this line and initialized res to zero and leaving the stack with root,1 so even if the root is null the if statement still catch null condition
            return 0

        q=deque([root])

        level=0

        while q:
            for i in range(len(q)):
                node=q.popleft()

                if node.right:
                    q.append(node.right)

                if node.left:
                    q.append(node.left)
            level+=1

        return level