'''
want to compare each word in the dictionary, the words are in order
input:
order of words
output:
order of alphabet in order in alien dictionary

edge case:
if there is a word that have the same prefix as the word above and
if it is longer it need to be shorter than the word above or else return res"" the rule break case
if no words return ""

approach:
get a hashtable to record the order precedence so we can traverse in the future
to compare the word by word we first need to go through a for loop of each of the string in the list
then we need to compare string by string, if the letter differ string 1 is map to string 2 's letter
if the string is the same continue
also check the edge case along the loop

then after we get the table set up we traverse from all the key in the table to see if there is a loop,
to check if there is a loop along the path we can use dfs and a visit set to record that path

'''


class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c:set() for word in words for c in word}


        if not words:
            return ""
        
        
        for i in range(len(words)-1):
            w1=words[i]
            w2=words[i+1]
            minlength=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:minlength]==w2[:minlength]:
                return ""
            
            for j in range(minlength):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
                
            
        visited = set()
        path = set()
        res = []

        def dfs(c)->bool:
            if c in visited:
                return True
            if c in path:
                return False
            path.add(c)
            for nei in adj[c]:
                if not dfs(nei):
                    return False
            path.remove(c)
            visited.add(c)
            res.append(c)
            return True
        
        for c in adj:
            if not dfs(c):
                return ""

        return "".join(res[::-1])


        
        
        