class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer = 0

        part_sums = []
        for i, n in enumerate(nums):
            if i > 0:
                part_sums.append(part_sums[i-1] + n)
            else:
                part_sums.append(n)
    
        sums = {}
        for s in part_sums:
            sums[s] = sums.get(s, 0) + 1

        left_sum = 0
        answer += sums.get(k, 0)
        for n in nums:
            left_sum += n
            if sums[left_sum] == 1:
                del sums[left_sum]
            else:
                sums[left_sum] -= 1
            
            answer += sums.get(k + left_sum, 0)
        
        return answer
    
    # speed = O(n^2) memory O(1)    
    def subarraySum2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        answer = 0

        sums = {0: 1}
        left_sum = 0
        for n in nums:
            left_sum += n
            answer += sums.get(left_sum - k, 0)
            sums[left_sum] = sums.get(left_sum, 0) + 1
        
        return answer
        
    
    # speed = O(n^2) memory O(1)

        

inp = [1,2,1]
#inp = [0,1,2,2]
#inp = [1,2,3,2,2]
#inp = [3,3,3,1,2,1,1,2,3,3,4] # 5

k = 3

print(Solution().subarraySum2(inp, k))

# blunt : all subarrays