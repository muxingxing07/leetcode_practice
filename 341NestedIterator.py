#1. �ڹ��캯���У�ջ����ŵ�Ӧ���� stack = [[2, 3], 1]
#2. �ڵ��� hasNext() ����ʱ������ջ��Ԫ���� 1��Ϊ int����ôֱ�ӷ��� true;
#3. Ȼ����� next() ����������ջ��Ԫ�� 1��
#4. �ٵ��� hasNext() ����ʱ������ջ��Ԫ���� [2,3]��Ϊ list����ô��Ҫ̯ƽ�������ŵ�ջ�С�
#        ��ǰ��ջ�� stack = [3, 2]
#5. Ȼ����� next() ����������ջ��Ԫ�� 2��
#6. Ȼ����� next() ����������ջ��Ԫ�� 3��
#7. �ٵ��� hasNext() ����ʱ��ջΪ�գ���˷��� false�����������н�����

#û�п�����Ŀ

# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        for i in range(len(nestedList) - 1, -1, -1):
            self.stack.append(nestedList[i])

    def next(self) -> int:
        cur = self.stack.pop()
        return cur.getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            cur = self.stack[-1]
            if cur.isInteger():
                return True
            self.stack.pop()
            for i in range(len(cur.getList()) - 1, -1, -1):
                self.stack.append(cur.getList()[i])
        return False