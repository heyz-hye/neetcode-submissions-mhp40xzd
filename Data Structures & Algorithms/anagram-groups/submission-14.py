class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        
        for x in strs:
            key = "".join(sorted(x))
            if key in seen:
                seen[key].append(x)
            else:
                seen[key]=[x]

        return list(seen.values())
        