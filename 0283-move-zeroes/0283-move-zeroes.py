class Solution:
    def moveZeroes(self, nums) :
        k=0
        for num in nums:
            if num!=0:
                nums[k]=num
                k+=1
                #here nums become [1,3,12,(3,12)] so we have to change or append zeros at last
        while k<len(nums):
            nums[k]=0
            k+=1

            
            
            
        