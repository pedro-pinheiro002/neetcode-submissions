class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen1 = {}
        seen2 = {}

        for ch1 in s:
            if seen1.get(ch1):
                seen1[ch1] += 1
            else:
                seen1[ch1] = 1

        for ch2 in t:
            if seen2.get(ch2):
                seen2[ch2] += 1
            else: 
                seen2[ch2] = 1
        print(seen1)
        print(seen2)
        return seen2 == seen1