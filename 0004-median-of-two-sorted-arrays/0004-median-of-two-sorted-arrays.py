class Solution:
   
    def findMedianSortedArrays(self,num1,num2): 
        

        merge=num1+num2
        merge.sort()

        length=len(merge)
        
        if length%2 == 0:
            
            median=(merge[length//2-1]+merge[(length//2)])/2
        else :

            median=merge[length//2]

        return median

        