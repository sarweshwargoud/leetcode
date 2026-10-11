class Solution:
    def frequencySort(self, s: str) -> str:
        has={}

        for st in s:
            has[st] = has.get(st, 0) + 1   # has.get give returns the value of that key "st"

        sorted_str=sorted(has,key=has.get,reverse=True) #sorted_str is a list which stores unique elements

        final=""

        for ch in sorted_str:
            final=final + ch*has[ch] #list has unique elemts right so for printng the repeated char as in input strigs multiply with their frequncy


            
        return final