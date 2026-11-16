class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for strin in strs:
            n = len(strin)
            res += str(n) + "#" + strin
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        length = ""
        while i < len(s):       
            if s[i] == "#":
                length = int(length)
                res.append(s[i+1:i+1+length])
                i += length
                length = ""
            else:
                length += s[i]
            i += 1
        return res
                