class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while(val in nums):
            nums.pop(nums.index(val))
        return len(nums)

##倒序遍历
class Solution:
    def removeElement(self,nums:List[int],val:int)->int:
        for i in range(len(nums)-1,-1,-1):
            if(nums[i]==val):
                nums.pop(i)
        return len(nums)