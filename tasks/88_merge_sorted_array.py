class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """ 
        nums1_cp = nums1[0:m]

        p1 = 0
        p2 = 0
        p_res = 0

        while p1 < m and p2 < n:
            el1 = nums1_cp[p1]
            el2 = nums2[p2]

            if el1 <= el2:
                nums1[p_res] = el1
                p1 += 1
            else:
                nums1[p_res] = el2
                p2 += 1
            p_res += 1

        if p1 < m:
            for el in nums1_cp[p1:m]:
                nums1[p_res] = el
                p_res += 1
    
        if p2 < n:
            for el in nums2[p2:n]:
                nums1[p_res] = el
                p_res += 1
        

nums1 = [1,2,3,0,0,0]; m = 3; nums2 = [2,5,6]; n = 3
Solution().merge(nums1, m, nums2, n)
print(nums1)

# 2 pointers 1 per array:
# a, b = 0
# copy array 1
# traverse arr1 copy + array 2, extract lower numbers first