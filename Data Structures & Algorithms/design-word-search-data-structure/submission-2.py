'''
this problem is quiet hard since there is a wildcard, the wildcare . can be any of the node's children.
so you need to use dfs to explore every node's children option if there is a wildcard for search

everything else is basically the same as regular Trie datastructure

Search function logic:
if the the index of the word given is equal to the length of the word, that mean we have pass in the last node that
is suppose to be telling us if the word end there. so we return the end attribute of that node, it can be True or False

if there is a letter that isnt mathcing with any of the nodes's children then we return false

if there is the index at word is a wildcard then we explore every single possible children of that node and if one of them returns
true, then we return true for the whole statement

else after the for loop end there isn't any matching we return false

if the letter is a matching letter a children of the node, we need have to call the function recursively to get to the end of the word
and return the result

we only need to check if one of the possibilities of the wild card return a True value aka if the word is in there we dont need to check if all the possibilities
stem from that wildcard return True
if no possibilities is viable return False
we also loop through key not value because value is a TrieNode 

time complexity:
O(N) for add word since word case you have to add every single letter of the word
O(26^N) for addWord. For search, O(N) if there are no wildcards, up to O(26^N) worst case with wildcards (imagine a query of all dots).

space complexity:
O(N) depth of the recursive stack equal to length of the word
O(26^N) recursion stack depth per branch; trie storage itself is O(total characters across all added words) independent of search.

question:but if one of them return true then why would we need to explore other children at that level?
Good question — you're right that if one child returns True, we stop immediately at that level and don't check the rest. That's the best case, and it's exactly why real-world performance is often way better than the worst-case bound.

But Big-O complexity describes the worst case — and the worst case for search is when the word is not in the trie, or matches only through the very last branch checked.

Think about search("....") in a trie where the word doesn't actually exist. To be certain it's not there, you have no choice but to try every single child at every level — because until you've exhausted all of them, you can't rule out that some deeper combination would have worked. Only after every branch at every level has failed can you correctly return False.

So:

Best case: first branch you try happens to succeed → fast, short-circuits immediately
Worst case: the word isn't in the trie at all (or only the last-checked path would've worked) → you're forced to explore everything → O(26^N)

'''

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
        def dfs(node,i)->bool:
            if i==len(word):
                return node.end
            
            if word[i]!="." and word[i] not in node.children:
                return False
            
            if word[i]==".":
                for val in node.children.values():
                    if dfs(val,i+1):
                        return True
                return False
            return dfs(node.children[word[i]],i+1)
        return dfs(self.root,0)



        
