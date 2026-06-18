class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique_num = set()

        for num in nums:
            if num in unique_num:
                unique_num.discard(num)
            else:
                unique_num.add(num)

        return list(unique_num)[0]