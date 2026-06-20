class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen=defaultdict(list)
        for i in strs:
            sor = "".join(sorted(i))
            seen[sor].append(i)
        return [ i for i in seen.values()]

                
            