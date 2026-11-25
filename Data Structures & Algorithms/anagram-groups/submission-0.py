class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        m = {}
        for s in strs:
            sort = "".join(sorted(s))
            m[sort] = m.get(sort, []) + [s]

        return [val for key, val in m.items()]
