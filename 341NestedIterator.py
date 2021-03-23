#1. 在构造函数中：栈里面放的应该是 stack = [[2, 3], 1]
#2. 在调用 hasNext() 方法时，访问栈顶元素是 1，为 int，那么直接返回 true;
#3. 然后调用 next() 方法，弹出栈顶元素 1；
#4. 再调用 hasNext() 方法时，访问栈顶元素是 [2,3]，为 list，那么需要摊平，继续放到栈中。
#        当前的栈是 stack = [3, 2]
#5. 然后调用 next() 方法，弹出栈顶元素 2；
#6. 然后调用 next() 方法，弹出栈顶元素 3；
#7. 再调用 hasNext() 方法时，栈为空，因此返回 false，迭代器运行结束。

#没有看懂题目

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