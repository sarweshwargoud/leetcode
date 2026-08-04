class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        # 1st find smallest and largest elements then after we can find lenth of array with missing element 
        # by using for loop from range sml to lrg with increment 1 we can check every elemt is present or not in array
        # initially we appended array elements into the hashmap for easy checking compared to array
        #they were more than 1 missing elemnets so ...have to append missing into array then return it
        

        sml=nums[0]
        lrg=nums[0]
        hsh={}
        hsh[nums[0]]=nums[0]

        for i in range(1,len(nums)):
            if nums[i]<sml:
                sml=nums[i]
            elif nums[i]>lrg:
                lrg=nums[i]
            hsh[nums[i]]=nums[i]
        leng=lrg-sml
        ans=[]
        
        for j in range(sml,lrg+1):
            if j not in hsh:
                ans.append(j)
        return ans
            

            
    
        