from functools import cmp_to_key
import math


def comparator(a, b):
    def def_cmp(x, y):
        if x<y:
            return 1
        elif x>y:
            return -1
        else:
            return 0
        
    a_first = int(a + b)
    b_first = int(b+a)
    return def_cmp(a_first, b_first)


class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        str_arr = list(map(str, nums))
        #key=lambda x:x*_max, reverse = True
        str_arr = sorted(str_arr, key=lambda x:x*math.ceil(10/len(x)), reverse=True)
        
        result = ''.join(str_arr).lstrip('0')
        return result if len(result) > 0 else '0'


nums = [10,2]
nums = [1, 11, 12, 14, 2]
nums = [3,30,34,5,9]
#nums = [0,0]

print(Solution().largestNumber(nums))

# 1, 11, 12, 14, 2 -> 2 14 12 11 (sort digit-wise)