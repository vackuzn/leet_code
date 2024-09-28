class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        if k == 1:
            return max(nums)
        
        current_sum = sum(nums[0:k])
        if k == len(nums):
            return float(current_sum) / k

        max_sum = current_sum

        for i in range(1, len(nums) - k + 1):
            current_sum -= nums[i-1]
            current_sum += nums[i + k - 1]
            max_sum = max(max_sum, current_sum)

        return float(max_sum) / k


inp = [1,2,3]
#inp = [0,1,2,2]
#inp = [1,2,3,2,2]
inp = [1,12,-5,-6,50,3]

print(Solution().findMaxAverage(inp, 4))

# [1,2,3,4,5] k = 2 -> (4+5)/2
# [1,2,3,2,1] k = 3 -> (2+3+2)/2
