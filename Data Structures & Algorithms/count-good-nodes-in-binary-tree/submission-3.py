'''
function call to check a node from the root is an eligible node that has no node in between that is greater
than the node being called. so we can do a bfs search every node we encounter, we check if a node is greater
than the node max value of that branch of the node. If the node is indeed greater we just increase count counter
by one and set max equal to that node and then we keep traversing left and right of that subtree. we return the
count variable. our compare function dont return anything because the we just compare and increase the counter
. To get into the loop we pass in root and float negative infinity to so that we make sure the max value is the smallest
so incase root is negative we can count it. By problem definition the root is always a good node
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count=0
        def dfs(node,maxval):
            if not node: #this is our stop condition or else we will encounter None.val error
                return
            if maxval<=node.val:
                self.count+=1
                maxval=node.val

            
            dfs(node.left,maxval)
            dfs(node.right,maxval)
        dfs(root,float('-inf'))
        return self.count
            
        