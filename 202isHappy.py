#ʹ�á�����ָ�롱˼�룬�ҳ�ѭ����ʹ�ü��ϣ����Ͽ��ܴﵽ�޷��洢��ʹ�õݹ飬�ݹ��ν�����ܵ��µ���ջ����
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

##ע��python������