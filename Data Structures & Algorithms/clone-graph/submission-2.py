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
        def dfs(node):
            if node in table: #there will always be node so noe is never null if a graph exist, stop infinite recursion because the node already existed
                return table[node]
            
            clone=Node(node.val)
            table[node]=clone
            for neigh in node.neighbors:
                clone.neighbors.append(dfs(neigh))
            
            return table[node]

        return dfs(node)


        