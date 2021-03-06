class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        for i in nums:
            if nums.count(i)==1:
                return i

##位运算：异或运算，相同的数异或为0，0异或任何数为任何数
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i == 0:
                res = nums[i]
            else:
                res ^= nums[i]

        return res
