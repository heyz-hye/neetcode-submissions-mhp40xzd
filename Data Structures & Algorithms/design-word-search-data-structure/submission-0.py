class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        
    def addWord(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        
        cur.end=True
        




    def search(self, word: str) -> bool:
        self
        def dfs(node,i)->bool:
            if i==len(word):
                return node.end
            
            if word[i]!="." and word[i] not in node.children:
                return False
            
            if word[i]==".":
                for key, val in node.children.items():
                    if dfs(val,i+1):
                        return True
                    
                return False
            return dfs(node.children[word[i]],i+1)
        return dfs(self.root,0)



        
