#使用“快慢指针”思想，找出循环，使用集合，集合可能达到无法存储，使用递归，递归层次较深，可能导致调用栈崩溃
class Solution:
    def isHappy(self, n: int) -> bool:
        def bitSquareSum(n):
            sumnum = 0
            while n > 0:
                bitnum = n % 10
                sumnum += bitnum * bitnum
                n = n // 10
            return sumnum

        slow = n
        fast = bitSquareSum(n)
        while slow != fast:
            slow = bitSquareSum(slow)
            fast = bitSquareSum(fast)
            fast = bitSquareSum(fast)
        return slow == 1

##注意python的整除