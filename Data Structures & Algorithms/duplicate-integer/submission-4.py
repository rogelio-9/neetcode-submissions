class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         
        '''
        initiate a set -> put i element in set -> if i in set
        return false -> else ->  return true
        '''

        unique = set()

        for num in nums:
            if num in unique:
                return True
            unique.add(num)
        return False