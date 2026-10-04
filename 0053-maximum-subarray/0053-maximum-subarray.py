class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        sum=0
        i=0
        max_sum=nums[i]
        for num in nums:

            sum=sum+num 

            max_sum=max(max_sum,sum)
            if sum<0:
                sum=0 # ekada manam sum=0 enduk ante ....incase if sum =0 or sum negative aythe dani tarvtha 
                    # oche nums add chesthe max ee untadi .....becz postive ....
                    # so manam -ve osthe sum ni 0 ki initalise chestham then further subarray sart at middle 
                    # [-2, 1, -3, 4, -1, 2, 1] ikada -2, 1, -3 ivi sum = -ve so sum=0 then after subarray start at 4 with max_sum
        return max_sum
        