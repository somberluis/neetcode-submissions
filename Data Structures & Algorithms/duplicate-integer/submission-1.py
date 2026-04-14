class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for x in nums:
            if x not in unique:
                unique.add(x)
            else:
                return True

        return False
