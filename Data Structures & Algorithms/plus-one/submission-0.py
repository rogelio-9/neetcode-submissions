class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_num = ""

        for num in digits:
            str_num += str(num)

        str_num = str(int(str_num) + 1)
        
        return [int(x) for x in str_num]