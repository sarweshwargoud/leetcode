class Solution:
    def isPalindrome(self, s):

        strr=""


        for i in s:
            if i.isalnum():
                strr=strr+i.lower()
        i=0
        j=len(strr)-1
        while(i<j):
            if strr[i]!= strr[j]:
                return False
            i+=1
            j-=1
        return True






        
       