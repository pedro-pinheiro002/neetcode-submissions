class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res += str(len(s)) + '#' + s
        return res
    
    def decode(self, s: str) -> List[str]:
        n = ''
        res = []
        i = 0
        while i < len(s):
            n += s[i]
            if s[i+1] == '#':
                n = int(n)
                res.append(s[i+2:i+2+n])
                i += n + 2
                n = ''
            else: 
                i += 1
        return res