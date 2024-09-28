class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        cnt = {}
        l=0
        r=0
        answer = 0

        for i, n in enumerate(fruits):            
            cnt[n] = cnt.get(n, 0) + 1

            while len(cnt) > 2:
                to_remove = fruits[l]
                cnt[to_remove] -= 1
                if cnt[to_remove] == 0:
                    del cnt[to_remove]
                l += 1

            answer = max(answer, i - l + 1)

        return answer

inp = [1,2,1]
inp = [0,1,2,2]
inp = [1,2,3,2,2]
inp = [3,3,3,1,2,1,1,2,3,3,4] # 5

print(Solution().totalFruit(inp))

        
# 1,2,1 -> 3
# 0,1,2,3 -> 2

# start from the beginning of the list
# add fruit types to the hashmap and increment right pointer 
# once cnt has more than 2 elements, increment left pointer and remove fruits till we have 2
# return max(r - l + 1)