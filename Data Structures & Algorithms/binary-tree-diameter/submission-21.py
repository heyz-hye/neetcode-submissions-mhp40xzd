'''
So the idea of the problem is pretty tricky for it to be classify as an easy
you want to calculate the diamater of each node and compare them throughout using
a max_diameter global variable. To find the maximum diameter of a node you need to find the maximum of node.left
height and the maximum of node.right's height. You then add 1+ both maximum to calculate the maximum diameter
of that node. Then you can return the maximum diameter since you go through every node. Run time should be O(n)
space complexity O(h)

also remember if you can store the recursion result in a variable so you don't have to compute twice by computing
the same thing again this save a lot of time

Also this is not an easy
Note: I confuse maximum diameter of a node with the maximum height of that node. These two are completely
different things don't confuse them

'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter=0
        def dfs(root):
            if not root:
                return 0
            
            left=dfs(root.left)
            right=dfs(root.right)

            self.diameter=max(self.diameter, left+right)

            return 1+max(left,right)
        dfs(root)
        return self.diameter

