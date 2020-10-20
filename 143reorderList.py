# 线性表，重构链表
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        temp = list()
        node = head
        while node:
            temp.append(node)
            node = node.next
        i, j = 0, len(temp) - 1

        while i < j:
            temp[i].next = temp[j]
            i += 1
            if i == j:
                break
            temp[j].next = temp[i]
            j -= 1
        temp[i].next = None


# 查找中点，翻转链表，链表拼接
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head or not head.next:
            return head
        end, slow, fast = head, head, head
        while fast and fast.next:
            end = slow
            slow = slow.next
            fast = fast.next.next
        end.next = None

        pre, cur = None, slow
        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp

        first, second = head, pre
        while first.next and second.next:
            temp2 = first.next
            first.next = second
            temp3 = second.next
            second.next = temp2
            first = temp2
            second = temp3
        if not first.next:
            first.next = second
        return head
