'''
zip create tuples
you can dict(a list of tuples)
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        smap={values:index for index, values in enumerate(inorder)}
        self.preorderindex=0
        def left2right(left, right)->TreeNode:
            if left >right:
                return None #left>right no nodes left to append
            mid=smap[preorder[self.preorderindex]]
            root=TreeNode(inorder[mid])
            self.preorderindex+=1

            root.left=left2right(left,mid-1)
            root.right=left2right(mid+1,right)
            return root
        return left2right(0,len(inorder)-1)

        