class Solution:

    def findMedianSortedArrays(self, nums1, nums2):
        la = 0
        lb = 0
        ra = len(nums1) - 1
        rb = len(nums2) - 1
        while la < ra and lb < rb:
            if nums1[la] < nums2[lb]:
                la += 1
            else:
                lb += 1
            if nums1[ra] > nums2[rb]:
                ra -= 1
            else:
                rb -= 1
        (la, lb, ra, rb, nums1, nums2) = (la, lb, ra, rb, nums1, nums2) if ra - la >= rb - lb else (lb, la, rb, ra, nums2, nums1)
        left = (ra + la) // 2
        x = nums1[left]
        if rb - lb < 0:
            right = left if (ra - la) % 2 == 0 else left + 1
            y = nums1[right]
            return round((x + y) / 2, 1)
        else:
            if (ra - la) % 2 == 0:
                if nums2[lb] == x:
                    y = x
                elif nums2[lb] < x:
                    y = nums1[left-1] if left - 1 >= la and nums2[lb] < nums1[left-1] else nums2[lb]
                else:
                    y = nums1[left+1] if left + 1 <= ra and nums2[lb] > nums1[left+1] else nums2[lb]
            else:
                if nums2[lb] < x:
                    y = x
                elif nums2[lb] > nums1[left+1]:
                    y = nums1[left+1]
                    x = y
                else:
                    y = nums2[lb]
                    x = y
            return round((x + y) / 2, 1)
