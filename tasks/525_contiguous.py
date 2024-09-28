class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        answer = 0

        if len(nums) < 2:
            return 0
        
        prev = {0: -1}
        
        left_sum = 0
        for i, n in enumerate(nums):
            val = 1 if n else -1
            left_sum += val
            if left_sum in prev:
                idx = prev[left_sum]
                answer = max(answer, i - idx)
            
            if left_sum not in prev:
                prev[left_sum] = i
        
        return answer
    
    def findMaxLength2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0

        if len(nums) < 2:
            return 0

        indices = [-2] * (len(nums) * 2 + 1)
        indices[len(nums)] = -1

        sum_left = 0
        for i, n in enumerate(nums):
            sum_left += 1 if n else -1
            if indices[len(nums) + sum_left] > -2:
                answer = max(answer, i - indices[len(nums) + sum_left])
            else:
                indices[len(nums) + sum_left] = i
        
        return answer
        


# 1,0,0,1,0 -> 4


inp = [1,0,1]
#inp = [0,1]
#inp = [0,1,1,0,1,1,1,1,1,1,0,0,0,0,0,0,0,]
#inp = [1,2,3,2,2]
#inp = [3,3,3,1,2,1,1,2,3,3,4] # 5

print(Solution().findMaxLength(inp), Solution().findMaxLength2(inp))

# blunt : all subarrays