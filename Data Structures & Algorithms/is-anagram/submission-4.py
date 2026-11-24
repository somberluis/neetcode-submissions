class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = {}
        for char in s:
            counts[char] = counts.get(char, 0) + 1

        counts_b = {}
        for char in t:
            counts_b[char] = counts_b.get(char, 0) + 1
        
        for key in counts:
            if counts[key] != counts_b.get(key, 0):
                print(key)
                print(counts[key], counts_b.get(key, 0))
                return False

        return True