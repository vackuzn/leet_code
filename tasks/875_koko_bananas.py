import math

class Solution(object):
    def minEatingSpeed2(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        biggest_pile_size = max(piles)
        if len(piles) == h:
            return biggest_pile_size
        
        k_min = 1
        k_max = biggest_pile_size

        while k_min < k_max:
            k_guess = (k_min + k_max) // 2

            hours_needed = sum([((p + k_guess - 1) // k_guess) for p in piles])  # O(n)
            if hours_needed > h: # increase k_guess
                k_min = k_guess + 1
            else:
                k_max = k_guess

        return k_min
    
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        biggest_pile_size = max(piles)
        if len(piles) == h:
            return biggest_pile_size
        
        k_min = 1
        k_max = biggest_pile_size
        res = 1

        while k_min <= k_max:
            k_guess = (k_min + k_max) // 2 
            h_current = sum([(n + k_guess - 1) // k_guess for n in piles])

            if h_current > h:
                k_min = k_guess + 1
            else:
                res = k_guess
                k_max = k_guess - 1
        
        return res

        # total O(nlog(n))
                

piles = [3,6,7,11]; h = 8 # 4
piles = [30,11,23,4,20]; h = 5 #Output: 30
#piles = [30,11,23,4,20]; h = 6 #Output: 23
#piles = [3,6,7,11]; h = 8 #Output: 4
print(Solution().minEatingSpeed(piles, h))

# if piles.len == h -> return max(piles)
# we need to find k so that
# sum(ceil(piles/k)) as close to h as possible but not exceeding it
# k: 1..max(piles)
# binary search to find optimal k