class Solution:
    def search(self, nums: List[int], target: int) -> int:

        mid=len(nums)//2
        low=0
        high=len(nums)-1

        if target < nums[low] or target > nums[high]:
            return -1

        while low<=high:
            mid=(low+high)//2
            if target==nums[mid]:
                return mid
            elif target>nums[mid]:
                low=mid+1
            else :
                high=mid-1
        return -1

            

        
        
        