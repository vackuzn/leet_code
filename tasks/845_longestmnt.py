class Solution(object):
    def longestMountain(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        longest = 0
        mnt_length = 1
        summit_reached = False

        if len(arr) < 3:
            return 0

        for i in range(len(arr) - 1):
            cur = arr[i]
            next = arr[i+1]

            if cur == next:
                mnt_length = 1
                summit_reached = False
                continue

            if cur < next: # going up
                if summit_reached:
                    mnt_length = 2
                    summit_reached = False
                else:
                    mnt_length += 1
            else: # going down
                if mnt_length < 2:
                    mnt_length = 1
                    summit_reached = False
                else:
                    summit_reached = True
                    mnt_length += 1
                    longest = max(longest, mnt_length)

        return longest
    
    def longestMountain2(self, arr) -> int:
        longest = 0
        up = 0
        down = 0

        for i in range(1, len(arr)):
            if (down and arr[i - 1] < arr[i]) or (arr[i - 1] == arr[i]):
                up = 0
                down = 0

            up += arr[i - 1] < arr[i]
            down += arr[i - 1] > arr[i]

            if up and down:
                longest = max(longest, up + down + 1)

        return longest  


inp = [
    # [2,1,4,7,3,2,5],
    # [0,1,2,3,4,5,6,7,8,9],
    # [1,2,3,2],
    # [2,2],
    # [10,2,5,10,9,1,1,4,3,7],
    # list(range(10000)),
    # [0,1,0,0,1,0,0,1,1,0,0,0,1,1,0,1,0,1,0,1,0,0,0,1,0,0,1,1,0,1,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,0,1,0,0,1,1,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,1,1,1,0,0,0,1,0,1,1],
    # [0,0,1,0,1,0,1,0],
    # [875,884,239,731,723,685],
    # [0,1,0],
    [9,8,7,6,5,4,3,2,1,0]
]

for i in inp:
    print(Solution().longestMountain(i), Solution().longestMountain2(i))
