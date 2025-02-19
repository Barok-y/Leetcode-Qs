class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        o=0
        for k in nums:
            if o==k:
                o+=1
            else:
                return o
        return o