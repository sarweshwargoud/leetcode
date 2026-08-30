class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        idxmx = nums.index(max(nums))
        idxmn = nums.index(min(nums))

        a = max(idxmx, idxmn) + 1
        b = n - min(idxmx, idxmn)
        c = idxmx + 1 + n - idxmn
        d = idxmn + 1 + n - idxmx

        return min(a, b, c, d)