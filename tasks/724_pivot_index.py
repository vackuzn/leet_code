class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # total sum
        sum = 0
        for n in nums:
            sum += n

        # iterating over array
        sleft = 0
        sright = sum
        for i, n in enumerate(nums):
            if i > 0:
                sleft += nums[i-1]
            sright -= n
            if sleft == sright:
                return i

        return -1



# 1,2,3,4,5 -> -1


inp = [1,7,3,6,5,6]

print(Solution().pivotIndex(inp))