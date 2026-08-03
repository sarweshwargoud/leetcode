class Solution:
    def twoSum(self, nums, target):

        hashmap = {}

        for i, num in enumerate(nums):

            complement = target - num
          
            if complement in hashmap:
                return [hashmap[complement], i]
                #store the value as key and indedx aas value in hashmap to search easily bcz hashmap checks key not value

            hashmap[num] = i