"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

thought process if there is no node we return None.
input given a node make a deep copy of each node and connect them

we can use a hashmap that map each node so that when we visit the same node again
we return and not call recursively any more
this problem is very similar to deep copy of random pointers for amazon

the hardest part is figuring what how to make a clone of the neighbors that haven't exist yet
run time: o(v for vertices plus edges for neighbors) 
space compelxity: o(h)height of the tree depth of the search and o(v) for amount of nodes in the hashmap

mistakes:

table[node].neighbors=node.neighbors
what is wrong with this part of the code?

answers: i am associating the orginal neighbors as the current copy's neighbors, we want
the copy node to associate with other clone neighbors not orignal neighbors

also calling dfs(i) twice on the same original node give two copy and hence an early 
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        table={}

        if not node:
            return None
        
        def dfs(node)->'Node':
            if node in table:
                return table[node] # this part is the core where you return the clone copy for the clone.neighbors
                                    #if the node already exist in hash table return table[node] the clone of that node
            
            clone=Node(node.val)
            table[node]=clone #map current node as key to a copy of the node
             

            for i in node.neighbors:
                clone.neighbors.append(dfs(i))
            return table[node] #if the node just exist in this original recursive call we return the clone copy back too
   
        return dfs(node) 



        