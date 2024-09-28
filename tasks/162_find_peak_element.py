class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, h = 0, len(nums) - 1
        
        while h > l:
            m = (h + l) // 2
            if nums[m] > nums[m+1]:
                h = m
            else:
                l = m + 1
        
        return l



nums = [1,2,3,1] # -> 2 the only peak, local maximum
#nums = [1,2,1,3,5,6,4] # -> 1, 5 return any
#nums = [1]
#nums = [1,2]
#nums = [2,1]
print(Solution().findPeakElement(nums))


# assume at least 1 peak exists? if not - check
# peak is at i == nums[i-1] < nums[i] and nums[i] > nums[i+1]
# linear solution - traverse till first peak -> arr[i-1] < arr[i] and arr[i] < arr[i+1]
# log(n) binary search