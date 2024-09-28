import math

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        min = 0
        max = n

        # find first bad version
        # while max - min >= 1:
        #     guess = math.floor((max + min) / 2)

        #     if isBadVersion(guess): # go left
        #         max = guess
        #     else: # go right
        #         min = guess + 1
        
        # return min

        # find last good version
        while max - min >= 1:
            guess = math.ceil((max + min) / 2)

            if isBadVersion(guess): # go left
                max = guess - 1
            else: # go right
                min = guess
        
        return min


        

def isBadVersion(version):
    return version >= 4
        
v = 15
print(Solution().firstBadVersion(v))

# blunt approach - linear traverse 1..n till first bad version is found, then return it O(n)
# smart approach - binary search - 1..n is sorted so can be used
# divide interval by half, is bad version = True -> go left, else go right