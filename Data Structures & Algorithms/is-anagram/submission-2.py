class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}

        for x in s:
            count[x] = count.get(x, 0) + 1

        for y in t:
            count[y] = count.get(y, 0) - 1


        for val in count.values():
            if val != 0:
                return False

        return True