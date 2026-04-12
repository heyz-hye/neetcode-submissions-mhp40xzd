class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for value in strs:
            key = "".join(sorted(value))
            if key in seen:
                seen[key].append(value)
            else:
                seen[key] = [value]
        return list(seen.values())