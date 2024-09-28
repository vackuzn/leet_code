class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        min_length = len(nums) + 1

        # if single element solution is available
        # if next((n for n in nums if n >= target), None) is not None:
        #     return 1
        
        l=0
        r=0
        cur_sum = nums[0]

        while True:
            # Expand
            if cur_sum < target:
                r += 1
                if r >= len(nums):
                    break
                cur_sum += nums[r]
                continue
            
            min_length = min(min_length, r - l + 1)
            cur_sum -= nums[l]
            l += 1

        return min_length if min_length <= len(nums) else 0        


target = 7
nums = [2,3,1,2,4,3]
nums = [1,4,4]
target = 4

print(Solution().minSubArrayLen(target,nums))

# 2,3,1,2,4,3 -> 4,3 -> 2
# 2,3,8,2,4,3 -> 8 -> 1

# if max(arr) >= target return 1;
#
# start at 0
# Expand:
# while arr[i:j] < target:
#   j++
# max = j - i + 1
# 
# Shrink
# while True:
# i++
# if sum(arr[i:j]) < target:
#   break
# max = j - i + 1
# 
# 