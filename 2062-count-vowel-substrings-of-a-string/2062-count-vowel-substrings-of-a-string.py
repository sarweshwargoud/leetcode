class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels=set("aeiou")
        ans=0


        for i in range(len(word)):

            seen=set()# this hash set should be created every iteration of i inedx chenaged  bcz for every iteration of i the new substings are counted from that i index
            for j in range(i,len(word)):

                if word[j] not in vowels:
                    break # used break bcz when constnats appear we have to stop bcz substring breaks
                seen.add(word[j])
                if len(seen)==5:#seen set contains unique elemets when we add seen.add(word[j]) stores uniqu char og vewels and we have only 5 vowelss so length dont exceed 5
                    ans=ans+1
        return  ans