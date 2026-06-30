"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        table={}
        
        if not node:
            return None
        
        def dfs(node)->Node:
            if node in table: #clone copy existed return that clone copy
                return table[node]
            
            clone=Node(node.val)
            table[node]=clone

            for i in range(len(node.neighbors)):
                clone.neighbors.append(dfs(node.neighbors[i])) # reason why we use dfs here is because the the clone copy we need to append hasnt been created yet
            
            return table[node] #return the clone copy that was just made in this called back to the original caller
        return dfs(node)


        