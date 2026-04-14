class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, x in enumerate(nums):
            remaining = target - x

            if remaining in seen:
                return [seen[remaining], idx]

            seen[x] = idx