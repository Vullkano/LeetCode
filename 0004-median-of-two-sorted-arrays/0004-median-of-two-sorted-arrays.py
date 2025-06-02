class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged_len = len(nums1) + len(nums2)
        is_even = merged_len % 2 == 0
        mid = merged_len // 2

        i = j = 0
        prev = curr = 0

        for _ in range(mid + 1):
            prev = curr
            if i < len(nums1) and (j >= len(nums2) or nums1[i] < nums2[j]):
                curr = nums1[i]
                i += 1
            else:
                curr = nums2[j]
                j += 1

        if is_even:
            return (prev + curr) / 2
        else:
            return curr