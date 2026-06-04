'''
So the idea of the problem is pretty tricky for it to be classify as an easy
you want to calculate the diamater of each node and compare them throughout using
a max_diameter global variable. To find the maximum diameter of a node you need to find the maximum of node.left
height and the maximum of node.right's height. You then add 1+ both maximum to calculate the maximum diameter
of that node. Then you can return the maximum diameter since you go through every node. Run time should be O(n)
space complexity O(2^N)


Note: I confuse maximum diameter of a node with the maximum height of that node. These two are completely
different things don't confuse them

'''
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0 

        def dfs(node):
            if not node:
                return 0
            current_diameter=dfs(node.left)+dfs(node.right)
            self.max_diameter=max(self.max_diameter, current_diameter)
            
            return 1+max(dfs(node.left),dfs(node.right))

        dfs(root)
        return self.max_diameter