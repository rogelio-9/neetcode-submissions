class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        idx_map = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in idx_map:
                return [idx_map[diff], i]
            idx_map[n] = i

