class Solution:
    def frequencySort(self, s: str) -> str:
        has={}

        for st in s:
            has[st] = has.get(st, 0) + 1

        sorted_str=sorted(has,key=has.get,reverse=True)

        final=""

        for ch in sorted_str:
            final=final + ch*has[ch]


            
        return final