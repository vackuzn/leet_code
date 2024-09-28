class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        lines = [''] * numRows
        going_down = True
        idx = 0

        for c in s:
            lines[idx] += c
            if idx == numRows - 1 or idx == 0:
                going_down = not going_down
            
            idx += -1 if going_down else 1

        return ''.join(lines)


        # period = 2 * (numRows - 1)
        # for i, c in enumerate(s):
        #     # up/down
        #     bucket_idx = i % period
        #     if bucket_idx >= numRows:
        #         bucket_idx = numRows - bucket_idx - 2
        #     lines[bucket_idx] += c

        # result = ""
        # for l in lines:
        #     for c in l:
        #         result += c

        # return result

s = "PAYPALISHIRING"; numRows = 3

print(Solution().convert(s, numRows))

# zig zag:
# solution 1: literally create 2d string array and fill chars, then print them line by line
# solution 2: find patterns
#ACEG
#BDFH
# case 1 - return string
# case 2 - return even then odd : delta = 2
# case 3:
# return 0, 4, 8 ... idx % 4, then odd then 2, 6, 8 ... 2 + idx % 4 ; delta = 4
# case 4:
# l1: 0 6 12 idx % 6; delta = 6
# l2: 1 + idx % 6 merge 5 + idx % 6
# l3: 2 + 
# l4: delta 8