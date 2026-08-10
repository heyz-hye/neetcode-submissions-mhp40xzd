'''
mistakes:
__init__self typo — not a real dunder, so TrieNode() never actually initializes children/end.
self.root read before assignment in PrefixTree.__init__ — needed self.root = TrieNode() instead.
cur never initialized in insert — missing the cur = self.root reset that you correctly included in search and startsWith.
cur.children() called as a function instead of accessed as a dict attribute (cur.children).

Trie datastructure:
root node point to start of a letter of a word, each TrieNode has a children table and a bool value
to see if it is end of a word

insert:
For each character in the word, if cur.children doesn't have that character yet, create a new TrieNode for it. 
Move cur to that child node (whether it already existed or was just created). 
By the end of the loop, cur points to the node representing the last character of the word — mark it as end = True.


Time Complexity:
O(1) loop up time because it is hashmap
O(N) for insert search and start with because it depend of the string parameter

Space Complexity:
Space is O(total characters across all inserted words) in the worst case 
— each new node stores one character's worth of branching, 
and shared prefixes reuse existing nodes rather than duplicating them.
if you do continue before you actually go through then you will skip transitioning cur into the next character for the word 
hence you check against the wrong TrieNode aka you stay at the same root TrieNode if c is indeed in the TrieNode's children

'''

class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False
    

class PrefixTree:
    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.end=True

    def search(self, word: str) -> bool:
        cur=self.root #reset the pointer
        for c in word:
            if c in cur.children:
                cur=cur.children[c]
            else:
                return False
        if not cur.end:
            return False
        return True
        
    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for c in prefix:
            if c in cur.children:
                cur=cur.children[c]
            else:
                return False
        return True
        
        