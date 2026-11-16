class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for word in strs:
            a = 26*[0]
            for ch in word:
                a[ord(ch) - ord("a")] += 1
            d[tuple(a)].append(word)
        
        return list(d.values())