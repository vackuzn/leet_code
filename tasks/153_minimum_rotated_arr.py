class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)

        l = 0
        h = nums_len * 2
        min_seen = 5001

        while True:
            m = (l+h) // 2
            cur_value = nums[m % nums_len]
            left_value = nums[(m-1) % nums_len]

            if left_value > cur_value:
                return cur_value
            
            if cur_value < min_seen:
                min_seen = cur_value
                h = m - 1
            else:
                l = m + 1
                        

nums = [3,4,5,1,2] # Output: 1
nums = [4,5,6,7,0,1,2] # Output: 0
nums = [11,13,15,17] # Output: 11
print(Solution().findMin(nums))

# O(n) -> foreach el in list: if el < min min = el
# O(Log(n))
# If array is shifted 0 times, just take leftmost element
# Array sorted asc + shift
# make circular buffer - join array to itself so it is a 2n array
# apply binary search to find element index i: nums[i-1]>nums[i]