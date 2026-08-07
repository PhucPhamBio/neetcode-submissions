class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = defaultdict(list)
        
        for word in strs:
            key = ''.join(sorted(word))
            dct[key].append(word)
        return list(dct.values())