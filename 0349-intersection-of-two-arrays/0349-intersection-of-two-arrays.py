class Solution:
    def intersection(self, nums1, nums2) :

        s=set(nums1)
        inter=set()# take two keys to storer the nums1 value(s) and common elements in both(inter)
        for num in nums2:#check each element in nums2 in hashset to know common elements in both the arrays
            if num in nums1:
                inter.add(num)
        return list(inter)
        