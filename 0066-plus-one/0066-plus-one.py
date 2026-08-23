class Solution:
    def plusOne(self, digits):
        num=0
        result=[]
        for digit in digits:
             num = num * 10 + digit
        num=num+1
        for ch in str(num):# to convert nu into string 
            result.append(int(ch))# append each string into each index in array
        return result


        

        


        