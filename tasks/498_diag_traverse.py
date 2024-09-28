class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        m = len(mat)
        n = len(mat[0])
        dir_up = True
        result = []

        # improve performance, get rid if extra enumeration

        # all diagonals
        for r in range(m+n):
            rng = range(r+1) if dir_up else reversed(range(r+1))
            for i in rng:
                row = r - i
                col = r - row
                if row < m and col < n:
                    result.append(mat[row][col])
            dir_up = not dir_up
        
        return result

        
inp = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().findDiagonalOrder(inp))

# diagonal is a manhattan distance circle
# radius grows from 0 to max(m,n) - 1
# need to remember direction, start with up