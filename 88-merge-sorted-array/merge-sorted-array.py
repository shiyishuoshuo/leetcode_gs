class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        copy_nums1 = nums1[0:m]
        i, j = 0, 0
        p = 0

        while i in range(m) and j in range(n):
            if copy_nums1[i] <= nums2[j]:
                nums1[p] = copy_nums1[i]
                p += 1
                i +=1
            else:
                nums1[p] = nums2[j]
                p += 1
                j +=1
        
        if i in range(m):
            while i in range(m):
                nums1[p] = copy_nums1[i]
                i += 1
                p +=1
            

        if j in range(n):
            while j in range(n):
                nums1[p] = nums2[j]
                j += 1
                p +=1
        