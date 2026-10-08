class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1

        l, r = 0, 0
        
        res = []
        while l < m and r < n:
            if nums1[l] <= nums2[r]:
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r += 1
        
        res += nums1[l:m] + nums2[r:n]
        nums1[:] = res