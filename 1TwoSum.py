class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, num in enumerate(nums):
            remaining = target - num
            if remaining in seen:
                return (seen[remaining], idx)
            else:
                seen[num] = idx