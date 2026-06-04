class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A)
        total = len(A) + len(B)
        half = (total+1) // 2
        while l <= r:
            i = (l + r) // 2
            j = half - i
            ALeft = A[i-1] if i > 0 else float('-inf')
            ARight = A[i] if i < len(A) else float('inf')
            BLeft = B[j - 1] if j > 0 else float('-inf')
            BRight = B[j] if j < len(B) else float('inf')

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2 == 1:
                    return max(ALeft, BLeft)
                else:
                    return (max(ALeft, BLeft) + min(ARight, BRight)) / 2

            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1

    