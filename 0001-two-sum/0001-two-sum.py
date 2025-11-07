class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num=list(enumerate(nums))
        num.sort(key=lambda x:x[1])
        i=0
        j=len(nums)-1
        while(i<j):
            sum=num[i][1]+num[j][1]
            if sum == target:
                return [num[i][0],num[j][0]]
            elif sum<target:
                i+=1
            else:
                j-=1
        return []